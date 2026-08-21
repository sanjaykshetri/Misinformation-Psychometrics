"""Initial item-level recovery models for Study 0B.

Observed responses are used to estimate person parameters first. Hidden
participant traits are loaded only for the final post-estimation comparison.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import expit


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


def main():
    veracity = pd.read_csv(DATA_DIR / "veracity_responses.csv")
    verification = pd.read_csv(DATA_DIR / "verification_responses.csv")
    participants = pd.read_csv(DATA_DIR / "participants.csv")

    veracity_estimates = fit_veracity_model(veracity)
    verification_estimates, _ = fit_verification_model(verification)
    estimates = veracity_estimates.merge(verification_estimates, on="participant_id")

    recovery = estimates.merge(
        participants[["participant_id", "discernment", "credulity_bias", "verification"]],
        on="participant_id",
        how="inner",
    )
    results = pd.DataFrame({
        "comparison": [
            "discernment",
            "response_bias_vs_credulity_bias",
            "verification",
        ],
        "estimate_column": [
            "estimated_discernment",
            "estimated_response_bias",
            "estimated_verification",
        ],
        "truth_column": ["discernment", "credulity_bias", "verification"],
        "correlation": [
            recovery["estimated_discernment"].corr(recovery["discernment"]),
            recovery["estimated_response_bias"].corr(recovery["credulity_bias"]),
            recovery["estimated_verification"].corr(recovery["verification"]),
        ],
    })
    estimates.to_csv(OUTPUT_PATH, index=False)
    print(results.to_string(index=False, float_format=lambda value: f"{value:.3f}"))
    print(f"\nSaved participant estimates to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
