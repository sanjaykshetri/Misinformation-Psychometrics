"""Study 0C: Monte Carlo robustness sweep for the Study 0B recovery models.

Repeats the item-level recovery pipeline (fit_veracity_model,
fit_verification_model, fit_updating_model, fit_evidence_comprehension_model
from model_recovery.py) on freshly simulated datasets generated under varied
data-generating conditions: sample size, item count, item difficulty spread,
response noise, carelessness rate, latent correlation strength, and (as of
this revision) a two-round updating item structure. Each condition varies one
factor away from the Study 0 baseline so degradation can be attributed to
that factor.

Each condition is run with REPLICATES independent seeds so that recovery is
reported as a mean +/- SD rather than a single point estimate.
"""

import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "simulation"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from simulate_misinformation_vulnerability_v1 import SEED, simulate_dataset  # noqa: E402
from model_recovery import (  # noqa: E402
    fit_evidence_comprehension_model,
    fit_updating_model,
    fit_veracity_model,
    fit_verification_model,
)

REPLICATES = 3
RAW_OUTPUT_PATH = Path(__file__).resolve().parent / "monte_carlo_results.csv"
SUMMARY_OUTPUT_PATH = Path(__file__).resolve().parent / "monte_carlo_summary.csv"

BASELINE = dict(
    n_participants=1000,
    n_veracity=40,
    n_updating=10,
    n_verification=10,
    difficulty_sd=0.75,
    noise_sd=1.0,
    careless_scale=1.0,
    corr_scale=1.0,
    updating_rounds=1,
)

# One factor is swept away from BASELINE per condition; replicate 0 of
# "baseline" reuses the canonical seed so it matches the main Study 0 dataset
# exactly.
SWEEPS = [
    ("baseline", {}),
    ("n_participants=250", {"n_participants": 250}),
    ("n_participants=2000", {"n_participants": 2000}),
    ("n_veracity=20", {"n_veracity": 20}),
    ("n_veracity=80", {"n_veracity": 80}),
    ("difficulty_sd=0.40", {"difficulty_sd": 0.40}),
    ("difficulty_sd=1.20", {"difficulty_sd": 1.20}),
    ("noise_sd=0.60", {"noise_sd": 0.60}),
    ("noise_sd=1.50", {"noise_sd": 1.50}),
    ("careless_scale=0.30", {"careless_scale": 0.30}),
    ("careless_scale=2.50", {"careless_scale": 2.50}),
    ("corr_scale=0.30", {"corr_scale": 0.30}),
    ("corr_scale=0.60", {"corr_scale": 0.60}),
    ("updating_rounds=2", {"updating_rounds": 2}),
]

RECOVERY_COLS = [
    "recovery_discernment",
    "recovery_response_bias",
    "recovery_verification",
    "recovery_updating",
    "recovery_evidence_evaluation",
]


def run_condition(name, overrides, seed):
    params = {**BASELINE, **overrides}
    data = simulate_dataset(seed=seed, **params)

    veracity_estimates = fit_veracity_model(data["veracity"])
    verification_estimates, _ = fit_verification_model(data["verification"])
    updating_estimates = fit_updating_model(data["updating"])
    comprehension_estimates = fit_evidence_comprehension_model(data["updating"])
    estimates = (
        veracity_estimates.merge(verification_estimates, on="participant_id")
        .merge(updating_estimates, on="participant_id")
        .merge(comprehension_estimates, on="participant_id")
    )

    recovery = estimates.merge(
        data["participants"][
            ["participant_id", "discernment", "credulity_bias", "verification", "updating", "evidence_evaluation"]
        ],
        on="participant_id",
        how="inner",
    )

    return {
        "condition": name,
        **params,
        "seed": seed,
        "recovery_discernment": recovery["estimated_discernment"].corr(recovery["discernment"]),
        "recovery_response_bias": recovery["estimated_response_bias"].corr(recovery["credulity_bias"]),
        "recovery_verification": recovery["estimated_verification"].corr(recovery["verification"]),
        "recovery_updating": recovery["estimated_updating"].corr(recovery["updating"]),
        "recovery_evidence_evaluation": recovery["estimated_evidence_evaluation"].corr(recovery["evidence_evaluation"]),
    }


def main():
    rows = []
    n_runs = len(SWEEPS) * REPLICATES
    run_i = 0
    for i, (name, overrides) in enumerate(SWEEPS):
        for rep in range(REPLICATES):
            seed = SEED if (name == "baseline" and rep == 0) else SEED + i * 1000 + rep
            t0 = time.time()
            row = run_condition(name, overrides, seed)
            row["replicate"] = rep
            rows.append(row)
            run_i += 1
            print(f"[{run_i}/{n_runs}] {name} (replicate {rep}) done in {time.time() - t0:.1f}s")

    results = pd.DataFrame(rows)
    results.to_csv(RAW_OUTPUT_PATH, index=False)

    summary = (
        results.groupby("condition")[RECOVERY_COLS]
        .agg(["mean", "std"])
        .reset_index()
    )
    summary.columns = ["condition"] + [f"{col}_{stat}" for col, stat in summary.columns[1:]]
    # groupby sorts conditions alphabetically; restore the intended sweep order.
    order = [name for name, _ in SWEEPS]
    summary["condition"] = pd.Categorical(summary["condition"], categories=order, ordered=True)
    summary = summary.sort_values("condition").reset_index(drop=True)
    summary.to_csv(SUMMARY_OUTPUT_PATH, index=False)

    print()
    print(summary.to_string(index=False, float_format=lambda v: f"{v:.3f}" if not np.isnan(v) else "NaN"))
    print(f"\nSaved {REPLICATES} replicate(s) per condition to {RAW_OUTPUT_PATH}")
    print(f"Saved condition summary (mean/SD) to {SUMMARY_OUTPUT_PATH}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
