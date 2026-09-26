# Study 0: A synthetic benchmark for misinformation psychometrics

## Introduction

Misinformation vulnerability is often studied as a single summary judgment, but this framing is theoretically limited. A more defensible psychometric account treats misinformation vulnerability as a multidimensional construct involving factual discernment, decision bias, confidence calibration, evidence evaluation, belief updating, verification competence, and sharing restraint. The present project asks whether these dimensions can be measured coherently and recovered from observed behavior under controlled conditions.

The synthetic simulation in Study 0 is designed as a methodological benchmark rather than a final empirical claim. It allows us to test the viability of the measurement architecture before introducing real human participants. In particular, the study addresses a basic question: to what extent can a theoretically specified multidimensional data-generating process be recovered from observed responses alone?

## Research question

Study 0 asks whether conventional psychometric summaries can recover the latent dimensions of misinformation vulnerability when the generating parameters are hidden during analysis. This is a blind-analysis problem. The latent variables are not used during model development. They are revealed only after the observed-only analysis to assess how well the observed metrics correspond to the generating structure.

## Methods

### Data-generating design

The synthetic dataset included 1,000 participants and a structured item bank spanning three task domains:

- 40 veracity items,
- 10 evidence-updating items,
- 10 verification items.

The generating model specified latent dimensions for:

- discernment,
- calibration,
- evidence evaluation,
- updating,
- verification skill,
- sharing restraint,
- general knowledge,
- credulity bias,
- contextual distortions,
- and careless responding.

This structure permits an analysis of whether the assessment can separate multiple processes that are frequently conflated in single-score approaches.

### Analysis procedure

The benchmark followed a strict observed-only workflow:

1. Load the response files and summary-score outputs.
2. Compute participant-level indicators from the observed data without using the hidden latent columns in participants.csv.
3. Compare the observed metrics with the known generating parameters after model estimation.

The outcome metrics included:

- veracity accuracy,
- true/false item accuracy,
- d-prime,
- response criterion,
- mean confidence,
- confidence-accuracy gap,
- Brier score,
- share rate,
- sharing restraint score,
- updating success rate,
- mean appropriate movement,
- verification accuracy,
- and careless-trial rate.

## Results

### Descriptive benchmark

The synthetic data generated a broad and interpretable range of behavior:

- average veracity accuracy: 0.605
- mean confidence: 83.314
- share rate: 0.419
- careless-trial rate: 0.057
- updating success rate: 0.764
- verification accuracy: 0.440

These values suggest that the simulation created sufficient variability for recovery to be measured while preserving realistic nuisance effects such as careless responding.

### Recovery of the hidden dimensions

The strongest observed relationships between latent generating traits and observed metrics were:

- discernment and d-prime: r = 0.932
- discernment and total accuracy: r = 0.924
- discernment and Brier score: r = -0.928
- sharing restraint and share rate: r = -0.929
- sharing restraint and sharing restraint score: r = 0.929
- carelessness and careless-trial rate: r = 0.906
- verification and verification accuracy: r = 0.827
- evidence evaluation and raw comprehension-check success rate: r = 0.718 (V1.1; see below)

Additional but weaker associations were also observed:

- updating and updating success rate: r = 0.553
- evidence evaluation and updating success rate: r = 0.504
- evidence evaluation and verification accuracy: r = 0.506
- general knowledge and d-prime: r = 0.458

### Item-level updating and evidence-comprehension models (Study 0B, V1.1)

The updating task was redesigned (V1.1) so that evidence comprehension is a directly observable comprehension-check response (`comprehension_correct`) rather than a hidden latent folded into the movement calculation — see the V1.1 revision note in [SIMULATION_SPEC_V1.md](../../simulation/SIMULATION_SPEC_V1.md) and the rationale in [docs/literature_review.md](../../docs/literature_review.md). Two separately-identified item-level models are now fit:

- `fit_evidence_comprehension_model`: a person-item (Rasch-style) IRT model fit directly to `comprehension_correct`, the same approach used for verification. On the baseline dataset this recovers `evidence_evaluation` at r = 0.707.
- `fit_updating_model`: a two-level (mixed-effects) model of `appropriate_movement` with evidence strength and the *within-person* deviation of `comprehension_correct` as fixed effects (a Mundlak-style within/between decomposition, needed because comprehension and updating are correlated traits and a naive shared slope on the raw response would steal between-person variance from the random intercept). This recovers `updating` at r = 0.383, matching the earlier summary-score-based estimate.

This is a substantial improvement over the V1 design, where evidence-evaluation recovery was only r = 0.133 and was frequently sign-reversed across Monte Carlo conditions (see below).

### Monte Carlo robustness sweep (Study 0C, V1.1, replicated)

The four item-level models (veracity, verification, updating, evidence comprehension) were re-fit on newly simulated datasets that each vary one factor away from the baseline: sample size (250-2,000), item count (20-80 veracity items), item difficulty spread, response noise, carelessness rate, and latent correlation strength — each run with 3 replicate seeds to estimate mean ± SD rather than a single point estimate. A 14th condition tests a two-round updating item design (see below). Full per-replicate results are in [monte_carlo_results.csv](monte_carlo_results.csv); the aggregated table is in [monte_carlo_summary.csv](monte_carlo_summary.csv).

- Discernment recovery is stable across all conditions (mean r = 0.88-0.94, SD ≤ 0.02).
- Response-bias recovery is stable but consistently moderate (mean r = 0.53-0.59).
- Verification recovery is stable (mean r = 0.78-0.84).
- Updating recovery ranges from mean r = 0.29 to 0.47 (SD up to 0.08, the largest relative spread of the five), generally improving with higher item difficulty spread, response noise, and weaker latent correlation.
- Evidence-evaluation recovery is stable and strong across every condition (mean r = 0.69-0.74, SD ≤ 0.03), with no sign reversals — a qualitative change from the V1 design, where the equivalent range included negative values.

**Two-round updating test.** To test whether a richer updating item structure improves recovery, each updating item was given a second, independent corrective-evidence exposure (starting from the round-1 post-judgment belief). Naively pooling both rounds' belief-movement data into the updating model *reduced* recovery (single-seed test: 0.383 → 0.277), because round 2 starts from an already-partially-corrected belief, compressing the available movement range and diluting the signal. Restricting movement scoring to round 1 while pooling both rounds' comprehension-check responses avoided this: updating recovery held steady (0.346 ± 0.032 vs. baseline's 0.346 ± 0.032 — statistically indistinguishable) while evidence-evaluation recovery improved further, from 0.716 ± 0.008 to 0.817 ± 0.011. `fit_updating_model` now auto-detects multi-round data and applies this restriction automatically.

The practical implication is that the current architecture is robust across a wide range of design choices for all five estimated quantities, and that adding comprehension-check opportunities (not repeated belief-revision opportunities) is the more promising direction for improving evidence-evaluation measurement further. Updating remains the dimension most in need of a genuinely different item design, not just more trials of the same kind.

## Discussion

The strongest results support the viability of a multidimensional measurement framework for misinformation vulnerability. The clearest recovery was in discernment, which is expected given that veracity discrimination is the central latent signal of the assessment. Sharing restraint and verification performance also showed robust alignment with their underlying generating dimensions, suggesting that these are separable behavioral domains rather than mere byproducts of overall accuracy.

The V1 design's weak, unstable recovery of evidence evaluation turned out to be a measurement-architecture artifact rather than an inherent property of the construct: once evidence comprehension was represented as its own directly observable response (V1.1) rather than a hidden latent buried inside the movement calculation, recovery became strong and stable across every Monte Carlo condition tested. This is a useful negative-then-positive result for the research program: it shows that "this dimension isn't recoverable" conclusions from a synthetic benchmark can reflect a fixable design flaw, and that fixing it is often cheaper in simulation than in a human pilot. Updating remains only moderately recoverable, which is itself informative — belief-revision quality appears to carry real but limited independent signal beyond comprehension and evidence strength, consistent with the continued-influence-effect/backfire-effect literature's caution that corrections do not reliably move beliefs by a fixed amount.

This pattern is consistent with the intended function of Study 0. The study is not meant to establish final construct validity. Rather, it reveals where the measurement architecture is strong and where it is conceptually or statistically entangled, and lets that entanglement be diagnosed and iterated on cheaply before human data collection. It therefore serves as a guide for the next stages of the research program.

## Limitations and future work

This study is deliberately limited to synthetic data. Its value lies in methodological stress testing, not in claims about real-world human performance. Updating recovery, while now well-identified via the within/between decomposition, remains only moderate (r = 0.26-0.55) — this may be a genuine property of how much independent signal belief-revision quality carries once comprehension and evidence strength are accounted for, or it may reflect that a single initial-judgment/correction/post-judgment cycle per item is still a thin design. Real human items should be developed from the continued-influence-effect and lateral-reading literatures (see [docs/literature_review.md](../../docs/literature_review.md)) rather than assumed from the current synthetic structure alone.

The next steps should prioritize:

1. testing whether a richer updating item structure (e.g., multiple evidence rounds, or an explicit weak-then-strong evidence sequence) improves updating recovery further,
2. item refinement for better construct discrimination, grounded in the literature synthesis,
3. a fully replicated Monte Carlo design with repeated-sampling variability at each condition,
4. and eventual validation in human samples, using real comprehension-check items modeled on the lateral-reading and continued-influence-effect paradigms.

## Conclusion

Study 0 shows that the proposed dimensions are computationally distinguishable under the specified synthetic data-generating assumptions. All five dimensions estimated by the item-level models are now recoverable from observed behavior with reasonable stability: discernment, verification skill, and sharing restraint most strongly, evidence evaluation strongly once measured through an observable comprehension-check response (V1.1), and updating moderately. This provides a clearer direction for human item design than the V1 benchmark did on its own.

The benchmark therefore supports continued development of the project. It does not yet provide evidence of human validity, but it provides the methodological justification for moving to more advanced psychometric modeling and eventual empirical data collection.
