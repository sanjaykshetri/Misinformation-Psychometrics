"""Item-level recovery models for Study 0B.

Observed responses are used to estimate person parameters first: a veracity
model (discernment, response bias), a binary IRT-style verification model,
a binary IRT-style evidence-comprehension model, and a two-level updating
model (evidence strength and the observed comprehension outcome as item/trial
predictors). Hidden participant traits are loaded only for the final
post-estimation comparison.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import expit
from statsmodels.regression.mixed_linear_model import MixedLM


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "simulated"
OUTPUT_PATH = ROOT / "studies" / "study_00_simulation" / "model_recovery_results.csv"


def _fit_logistic_person_item(y, person_index, item_index, n_persons, n_items, person_penalty=0.05):
    """Fit a two-stage Rasch-style model with observed item difficulties."""
    person_index = np.asarray(person_index, dtype=int)
    item_index = np.asarray(item_index, dtype=int)
    y = np.asarray(y, dtype=float)

    item_rates = np.bincount(item_index, weights=y, minlength=n_items)
    item_counts = np.bincount(item_index, minlength=n_items)
    item_rates = np.clip(item_rates / item_counts, 0.02, 0.98)
    item = -np.log(item_rates / (1.0 - item_rates))
    person = np.zeros(n_persons)
    for participant in range(n_persons):
        mask = person_index == participant

        def objective(value):
            eta = value[0] - item[item_index[mask]]
            log_likelihood = np.sum(y[mask] * eta - np.logaddexp(0.0, eta))
            return -log_likelihood + person_penalty * value[0] ** 2

        result = minimize(objective, np.zeros(1), method="BFGS")
        if not result.success:
            raise RuntimeError(f"Verification model did not converge for participant {participant}")
        person[participant] = result.x[0]

    person -= person.mean()
    item -= item.mean()
    return person, item


def fit_veracity_model(veracity):
    """Estimate discernment and response bias from item-level judgments.

    The response model is logit P(response_true) = item intercept + bias_i
    + truth_status * discernment_i. Centering and weak penalties regularize
    the person parameters for this initial benchmark.
    """
    data = veracity.sort_values(["participant_id", "item_id"]).copy()
    estimates = []
    for participant_id, group in data.groupby("participant_id", sort=True):
        truth = group["truth_status"].to_numpy(float)
        response = group["response_true"].to_numpy(float)

        def objective(parameters):
            bias, discernment = parameters
            eta = bias + truth * discernment
            log_likelihood = np.sum(response * eta - np.logaddexp(0.0, eta))
            penalty = 0.05 * (bias**2 + discernment**2)
            return -log_likelihood + penalty

        result = minimize(objective, np.zeros(2), method="BFGS")
        if not result.success:
            raise RuntimeError(f"Veracity model did not converge for {participant_id}: {result.message}")
        estimates.append((participant_id, result.x[1], result.x[0]))

    estimates = pd.DataFrame(
        estimates,
        columns=["participant_id", "estimated_discernment", "estimated_response_bias"],
    )
    estimates["estimated_discernment"] -= estimates["estimated_discernment"].mean()
    estimates["estimated_response_bias"] -= estimates["estimated_response_bias"].mean()
    return estimates


def fit_verification_model(verification):
    """Estimate verification ability and item difficulty from binary items."""
    data = verification.sort_values(["participant_id", "item_id"]).copy()
    participant_codes, participant_values = pd.factorize(data["participant_id"])
    item_codes, _ = pd.factorize(data["item_id"])
    ability, difficulty = _fit_logistic_person_item(
        data["correct"].to_numpy(float),
        participant_codes,
        item_codes,
        len(participant_values),
        data["item_id"].nunique(),
    )
    return pd.DataFrame({
        "participant_id": participant_values,
        "estimated_verification": ability,
    }), difficulty


def fit_evidence_comprehension_model(updating):
    """Estimate evidence-evaluation ability from observed comprehension checks.

    comprehension_correct is a directly observed per-trial response (did the
    participant correctly grasp the corrective evidence?), so this reuses the
    same person-item logistic model as verification rather than inferring the
    trait indirectly from belief-movement noise. Uses `trial_id` instead of
    `item_id` when present, so that multi-round updating data (where the same
    item_id appears twice with different evidence parameters) treats each
    round as its own item rather than averaging over both.
    """
    data = updating.sort_values(["participant_id", "item_id"]).copy()
    trial_col = "trial_id" if "trial_id" in data.columns else "item_id"
    participant_codes, participant_values = pd.factorize(data["participant_id"])
    item_codes, _ = pd.factorize(data[trial_col])
    ability, _ = _fit_logistic_person_item(
        data["comprehension_correct"].to_numpy(float),
        participant_codes,
        item_codes,
        len(participant_values),
        data[trial_col].nunique(),
    )
    return pd.DataFrame({
        "participant_id": participant_values,
        "estimated_evidence_evaluation": ability,
    })


def fit_updating_model(updating):
    """Estimate belief-revision quality from a two-level movement model.

    Fixed effects are the observed evidence strength (an item property) and
    the *within-person* deviation of comprehension_correct (a trial-level
    response, not the hidden evidence_evaluation trait). Comprehension and
    updating are correlated traits, so comprehension_correct's per-person
    mean is deliberately left out of the fixed effects (a Mundlak-style
    within/between decomposition): otherwise a single shared slope on the raw
    trial-level response would conflate the item-level effect of
    comprehension with the between-person variance that the random intercept
    is meant to capture, suppressing the updating-ability estimate.

    If a `round` column is present (multi-round updating items), only round 1
    is used for movement scoring: later rounds start from an
    already-partially-corrected belief, which compresses the available
    movement range and dilutes rather than sharpens the updating estimate
    (confirmed empirically; see docs/project_status.md). Evidence-comprehension
    scoring does not have this problem and should still use all rounds via
    fit_evidence_comprehension_model.
    """
    data = updating.copy()
    if "round" in data.columns:
        data = data[data["round"] == 1].copy()
    data["evidence_strength_c"] = data["evidence_strength"] - data["evidence_strength"].mean()
    person_mean_comprehension = data.groupby("participant_id")["comprehension_correct"].transform("mean")
    data["comprehension_within"] = data["comprehension_correct"] - person_mean_comprehension

    model = MixedLM.from_formula(
        "appropriate_movement ~ evidence_strength_c + comprehension_within",
        groups="participant_id",
        data=data,
    )
    fit = model.fit(reml=True)

    rows = []
    for participant_id, effects in fit.random_effects.items():
        intercept_re = effects.iloc[0]
        rows.append({
            "participant_id": participant_id,
            "estimated_updating": fit.fe_params["Intercept"] + intercept_re,
        })
    return pd.DataFrame(rows)


def main():
    veracity = pd.read_csv(DATA_DIR / "veracity_responses.csv")
    verification = pd.read_csv(DATA_DIR / "verification_responses.csv")
    updating = pd.read_csv(DATA_DIR / "updating_responses.csv")
    participants = pd.read_csv(DATA_DIR / "participants.csv")

    veracity_estimates = fit_veracity_model(veracity)
    verification_estimates, _ = fit_verification_model(verification)
    updating_estimates = fit_updating_model(updating)
    comprehension_estimates = fit_evidence_comprehension_model(updating)
    estimates = (
        veracity_estimates.merge(verification_estimates, on="participant_id")
        .merge(updating_estimates, on="participant_id")
        .merge(comprehension_estimates, on="participant_id")
    )

    recovery = estimates.merge(
        participants[["participant_id", "discernment", "credulity_bias", "verification", "updating", "evidence_evaluation"]],
        on="participant_id",
        how="inner",
    )
    results = pd.DataFrame({
        "comparison": [
            "discernment",
            "response_bias_vs_credulity_bias",
            "verification",
            "updating",
            "evidence_evaluation",
        ],
        "estimate_column": [
            "estimated_discernment",
            "estimated_response_bias",
            "estimated_verification",
            "estimated_updating",
            "estimated_evidence_evaluation",
        ],
        "truth_column": ["discernment", "credulity_bias", "verification", "updating", "evidence_evaluation"],
        "correlation": [
            recovery["estimated_discernment"].corr(recovery["discernment"]),
            recovery["estimated_response_bias"].corr(recovery["credulity_bias"]),
            recovery["estimated_verification"].corr(recovery["verification"]),
            recovery["estimated_updating"].corr(recovery["updating"]),
            recovery["estimated_evidence_evaluation"].corr(recovery["evidence_evaluation"]),
        ],
    })
    estimates.to_csv(OUTPUT_PATH, index=False)
    print(results.to_string(index=False, float_format=lambda value: f"{value:.3f}"))
    print(f"\nSaved participant estimates to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
