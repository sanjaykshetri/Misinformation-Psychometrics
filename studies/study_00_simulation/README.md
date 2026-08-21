# Study 0: blind-analysis simulation benchmark

This study uses the synthetic simulation as a measurement-recovery benchmark.

## Objective

To determine whether a multidimensional misinformation-vulnerability construct can be recovered from observed task responses when the generating parameters are hidden during analysis.

## Blind-analysis workflow

1. Study 0A loads the observed response files only.
2. Study 0A computes summary measures and writes observed estimates.
3. Study 0B fits item-level recovery models without loading participants.csv.
4. Only after estimation does the recovery phase load the hidden generating parameters.
5. Quantify recovery accuracy, contamination, and dimensional entanglement.

## Preliminary results

The synthetic benchmark shows the clearest recovery for discernment and sharing restraint, with strong correspondence between latent skill and observed performance metrics. Verification accuracy also tracks the hidden verification dimension closely. Updating and evidence evaluation are recoverable but less cleanly separated from general response quality. These are recovery results under programmed data-generating assumptions, not construct-validity evidence.

The full summary is available in [study_00_results.md](study_00_results.md).

## Important principle

This is a simulation for methodological stress testing, not for claiming human construct validity.

The output of Study 0 is not a final measure. It is a diagnostic check that the proposed assessment architecture is coherent enough to justify more expensive human-data collection.

## Study 0B: item-level model recovery

Run `model_recovery.py` after Study 0A. The first-pass models estimate participant discernment and response bias from item-level veracity judgments, and participant verification ability from item-level binary verification outcomes. The script then performs the post-estimation comparison with the hidden simulated traits. Updating is intentionally reserved for a longitudinal multilevel model rather than forced into a standard IRT score.
