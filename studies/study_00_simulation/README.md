# Study 0: blind-analysis simulation benchmark

This study uses the synthetic simulation as a measurement-recovery benchmark.

## Objective

To determine whether a multidimensional misinformation-vulnerability construct can be recovered from observed task responses when the generating parameters are hidden during analysis.

## Blind-analysis workflow

1. Load the observed response files only.
2. Fit the scoring or measurement model without using the latent generating variables.
3. Estimate latent traits or summary measures from the observed data.
4. Compare the estimated structure to the hidden generating parameters in participants.csv.
5. Quantify recovery accuracy, contamination, and dimensional entanglement.

## Preliminary results

The synthetic benchmark shows the clearest recovery for discernment and sharing restraint, with strong correspondence between latent skill and observed performance metrics. Verification accuracy also tracks the hidden verification dimension closely. Updating and evidence evaluation are recoverable but less cleanly separated from general response quality.

The full summary is available in [study_00_results.md](study_00_results.md).

## Important principle

This is a simulation for methodological stress testing, not for claiming human construct validity.

The output of Study 0 is not a final measure. It is a diagnostic check that the proposed assessment architecture is coherent enough to justify more expensive human-data collection.
