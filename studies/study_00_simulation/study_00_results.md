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
- updating success rate: 0.761
- verification accuracy: 0.445

These values suggest that the simulation created sufficient variability for recovery to be measured while preserving realistic nuisance effects such as careless responding.

### Recovery of the hidden dimensions

The strongest observed relationships between latent generating traits and observed metrics were:

- discernment and d-prime: r = 0.932
- discernment and total accuracy: r = 0.924
- discernment and Brier score: r = -0.928
- sharing restraint and share rate: r = -0.929
- sharing restraint and sharing restraint score: r = 0.929
- carelessness and careless-trial rate: r = 0.906
- verification and verification accuracy: r = 0.829

Additional but weaker associations were also observed:

- updating and updating success rate: r = 0.545
- evidence evaluation and updating success rate: r = 0.510
- evidence evaluation and verification accuracy: r = 0.504
- general knowledge and d-prime: r = 0.458

## Discussion

The strongest results support the viability of a multidimensional measurement framework for misinformation vulnerability. The clearest recovery was in discernment, which is expected given that veracity discrimination is the central latent signal of the assessment. Sharing restraint and verification performance also showed robust alignment with their underlying generating dimensions, suggesting that these are separable behavioral domains rather than mere byproducts of overall accuracy.

The moderate recovery for updating and evidence evaluation is more informative than discouraging. It suggests that these constructs are not trivially recoverable from simple summary scores alone and that additional model structure is needed to distinguish evidence-based revision from general accuracy and confidence behavior. In other words, the synthetic benchmark indicates that the conceptual distinction is valid, but the current measurement approach is not yet fully sufficient to recover those dimensions cleanly in a single-stage summary analysis.

This pattern is consistent with the intended function of Study 0. The study is not meant to establish final construct validity. Rather, it reveals where the measurement architecture is strong and where it is conceptually or statistically entangled. It therefore serves as a guide for the next stages of the research program.

## Limitations and future work

This study is deliberately limited to synthetic data. Its value lies in methodological stress testing, not in claims about real-world human performance. The summary metrics used here are coarse and may obscure important multidimensional relationships. In particular, updating and evidence evaluation appear partially confounded with general response quality and confidence-driven behavior under the current scoring regime.

The next steps should prioritize:

1. more explicit separation of updating and evidence evaluation,
2. multi-dimensional scoring or latent-variable modeling,
3. item refinement for better construct discrimination,
4. and eventual validation in human samples.

## Conclusion

Study 0 demonstrates that the proposed misinformation-vulnerability framework is structurally coherent under known synthetic conditions. The strongest dimensions are recoverable from observed behavior, especially discernment, verification skill, and sharing restraint. More subtle dimensions such as updating and evidence evaluation remain partially entangled, which provides a clear direction for future refinement.

The benchmark therefore supports continued development of the project. It does not yet provide evidence of human validity, but it provides the methodological justification for moving to more advanced psychometric modeling and eventual empirical data collection.
