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

The synthetic benchmark shows the clearest recovery for discernment and sharing restraint, with strong correspondence between latent skill and observed performance metrics. Verification accuracy also tracks the hidden verification dimension closely. The item-level updating model recovers the updating trait moderately (r ~ 0.26-0.55 across conditions). Evidence evaluation, once redesigned (V1.1) to use an observable comprehension-check response instead of a hidden latent, recovers well and stably (r ~ 0.68-0.75 across all Study 0C conditions, no sign reversals). These are recovery results under programmed data-generating assumptions, not construct-validity evidence.

The full summary is available in [study_00_results.md](study_00_results.md).

## Important principle

This is a simulation for methodological stress testing, not for claiming human construct validity.

The output of Study 0 is not a final measure. It is a diagnostic check that the proposed assessment architecture is coherent enough to justify more expensive human-data collection.

## Study 0B: item-level model recovery

Run `model_recovery.py` after Study 0A. The models estimate participant discernment and response bias from item-level veracity judgments, participant verification ability from item-level binary verification outcomes, belief-updating quality from a two-level (mixed-effects) model of belief movement with evidence strength as an item-level predictor, and evidence-evaluation ability from a person-item IRT-style model fit directly to the observed comprehension-check responses (V1.1). The script then performs the post-estimation comparison with the hidden simulated traits.

## Study 0C: Monte Carlo robustness sweep

Run `study_00c_monte_carlo.py` after Study 0B. It repeats the same recovery pipeline on freshly simulated datasets under varied conditions (sample size, item count, item difficulty spread, response noise, carelessness rate, latent correlation strength), one factor away from the Study 0 baseline per condition, and writes per-condition recovery correlations to `monte_carlo_results.csv`. This is a first-pass sensitivity sweep rather than a fully replicated Monte Carlo design with repeated-sampling variability at each condition.
