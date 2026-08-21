# Research roadmap

## Study 0: synthetic benchmark and recovery analysis

Purpose: assess whether a theoretically motivated multidimensional construct can be recovered from observed responses under known data-generating conditions.

Key questions:

- Can latent dimensions be distinguished psychometrically?
- Which conventional methods recover the simulated structure most accurately?
- Which dimensions remain entangled under realistic noise and carelessness?

### Study 0A: descriptive observed-only benchmark

Compute participant summaries and save observed estimates without loading the latent generating parameters.

### Study 0B: item-level model recovery

Fit item-level models before revealing the simulated truth:

- a veracity model with separate participant discernment and response-bias parameters,
- a binary item-response model for verification ability,
- and a longitudinal multilevel updating model with evidence strength and complexity as item predictors.

Compare estimated traits with the generating values only in a post-estimation recovery phase. The first two models are implemented as an initial benchmark in `studies/study_00_simulation/model_recovery.py`; updating remains a planned extension because its initial-belief to evidence to post-belief structure is not adequately represented by a conventional binary IRT score.

### Study 0C: Monte Carlo robustness

Repeat Study 0B across sample size, item count, item difficulty, response noise, carelessness, and latent correlation conditions before beginning human item development.

## Study 1: item and instrument development

Purpose: translate the construct into a human-facing assessment protocol.

Core tasks:

- refine item wording and topic coverage,
- pilot response formats for veracity, updating, and verification tasks,
- assess item difficulty and discrimination,
- separate construct-relevant signals from response style effects.

## Study 2: human validation and psychometrics

Purpose: estimate measurement quality in real samples.

Core tasks:

- reliability estimation,
- factor structure evaluation,
- measurement invariance checks,
- convergent and discriminant validity analysis,
- calibration of confidence reporting.

## Study 3: predictive validity

Purpose: investigate whether the measurement model predicts downstream behaviors such as sharing, belief formation, or susceptibility to misinformation exposure.

## Study 4: applied modeling and intervention support

Purpose: use validated measures to understand who is most vulnerable and under what circumstances, with attention to decision-support and media-literacy interventions.

## Research principle

The project proceeds from a measurement-first logic. Synthetic benchmarks are used to stress-test design assumptions before drawing conclusions about real-world populations.
