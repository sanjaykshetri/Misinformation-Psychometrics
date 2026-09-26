# Project status report and roadmap

Date: 2026-09-26

## 1. What this project is

Misinformation Psychometrics is a research program to conceptualize, measure, and
model individual differences in vulnerability to misinformation as a
multidimensional construct (discernment, response bias, calibration, evidence
evaluation, updating, verification competence, sharing restraint), rather than a
single "fake-news score." See [construct_definition.md](construct_definition.md)
for the full conceptual model.

The program is staged: Study 0 (synthetic benchmark) → Study 1 (item/pilot
development) → Study 2 (human psychometric validation) → Study 3 (predictive
validity) → Study 4 (applied/intervention). This report covers what has been
completed in Study 0 and what standard psychometric research practice implies
for the next stage.

## 2. What has been done

### 2.1 Construct and simulation design

- The construct is defined and documented ([construct_definition.md](construct_definition.md)).
- A synthetic data-generating model is specified ([SIMULATION_SPEC_V1.md](../simulation/SIMULATION_SPEC_V1.md)) and implemented
  ([simulate_misinformation_vulnerability_v1.py](../simulation/simulate_misinformation_vulnerability_v1.py)), producing 1,000 simulated
  participants responding to 40 veracity items, 10 belief-updating items, and 10
  verification items, plus per-participant summary scores.
- The generator is now refactored into a parameterized `simulate_dataset(...)`
  function (sample size, item counts, item difficulty spread, response noise,
  carelessness rate, latent correlation strength), which the Study 0C sweep
  below depends on. Calling it with defaults reproduces the original benchmark
  dataset's diagnostics exactly.

### 2.2 Study 0A — observed-only descriptive benchmark

Participant-level summary scores (accuracy, d-prime, criterion, confidence-accuracy
gap, Brier score, share rate, updating success rate, verification accuracy) are
computed from observed responses only, with the generating parameters hidden
until a later comparison step. See [01_simulation_eda.ipynb](../notebooks/01_simulation_eda.ipynb).

### 2.3 Study 0B — item-level recovery models

Implemented in [model_recovery.py](../studies/study_00_simulation/model_recovery.py), fit without using hidden
participant traits:

| Model | Method | Recovers | Correlation with hidden truth |
|---|---|---|---|
| Veracity | Per-participant penalized MLE (bias + discernment) | Discernment | r = 0.927 |
| Veracity | same model | Response bias vs. credulity bias | r = 0.549 |
| Verification | Person-item (Rasch-style) MLE | Verification ability | r = 0.816 |
| Evidence comprehension (V1.1) | Person-item (Rasch-style) MLE fit to the observed `comprehension_correct` response | Evidence-evaluation trait | r = 0.707 |
| Updating | Two-level (`MixedLM`) model on belief movement, with evidence strength and the within-person deviation of comprehension_correct as fixed effects, per-participant random intercept | Updating trait | r = 0.383 |

The updating model was the one piece of Study 0B originally left as a
placeholder. Its first implementation confirmed, at the item level rather than
just via summary scores, that evidence evaluation was not cleanly separable
from updating (r = 0.133, frequently sign-reversed). That measurement design
has since been fixed (V1.1, see below): evidence comprehension is now a
directly observable comprehension-check response rather than a hidden latent,
and is fit with its own model, raising its recovery to r = 0.707 while
updating recovery held steady.

### V1.1 redesign: evidence comprehension made observable

Following the continued-influence-effect literature's separation of
comprehending a correction from acting on it (see [literature_review.md](literature_review.md)), the
updating task was redesigned so that:

- participants now emit an observable binary `comprehension_correct` response
  (a noisy realization of the same underlying comprehension signal that also
  drives belief movement), replacing a hidden `evidence_comprehension_latent`
  column that a real assessment could never have observed;
- `fit_evidence_comprehension_model` estimates evidence-evaluation ability
  directly from that observed response, the same way verification ability is
  estimated, instead of inferring it indirectly as a side effect of movement
  noise;
- `fit_updating_model` uses a within/between (Mundlak-style) decomposition of
  `comprehension_correct`, which was necessary because comprehension and
  updating are correlated traits — a naive shared slope on the raw response
  conflated the two and suppressed the updating estimate (r dropped to 0.165
  during development before this fix).

This also fixed an unrelated bug where the simulation wrote its output CSVs
into `simulation/` instead of `data/simulated/`, closing the data-provenance
gap noted below.

### 2.4 Study 0C — Monte Carlo robustness sweep

Implemented in [study_00c_monte_carlo.py](../studies/study_00_simulation/study_00c_monte_carlo.py): a one-factor-at-a-time
sensitivity sweep re-running the Study 0B models on freshly simulated datasets
that each vary one generating condition away from baseline. Full results in
[monte_carlo_results.csv](../studies/study_00_simulation/monte_carlo_results.csv).

| Factor varied | Discernment r | Response-bias r | Verification r | Updating r | Evidence-evaluation r |
|---|---|---|---|---|---|
| Baseline (n=1000, 40 items) | 0.927 | 0.549 | 0.816 | 0.383 | 0.707 |
| n = 250 | 0.913 | 0.507 | 0.832 | 0.382 | 0.708 |
| n = 2000 | 0.917 | 0.525 | 0.815 | 0.357 | 0.736 |
| 20 veracity items | 0.891 | 0.538 | 0.828 | 0.382 | 0.697 |
| 80 veracity items | 0.933 | 0.548 | 0.795 | 0.441 | 0.720 |
| Narrower item difficulty | 0.907 | 0.571 | 0.836 | 0.338 | 0.740 |
| Wider item difficulty | 0.927 | 0.551 | 0.811 | 0.551 | 0.721 |
| Lower response noise | 0.899 | 0.531 | 0.834 | 0.264 | 0.736 |
| Higher response noise | 0.914 | 0.497 | 0.836 | 0.438 | 0.717 |
| Lower carelessness | 0.936 | 0.543 | 0.843 | 0.423 | 0.748 |
| Higher carelessness | 0.871 | 0.490 | 0.785 | 0.398 | 0.684 |
| Weaker latent correlation | 0.901 | 0.550 | 0.778 | 0.392 | 0.710 |
| Moderately weaker latent correlation | 0.909 | 0.562 | 0.810 | 0.394 | 0.713 |

**Conclusion:** all five estimated quantities are now stable in sign and
magnitude across every condition tested. Discernment, response bias, and
verification recovery were already stable in the V1 design. Evidence-evaluation
recovery (r = 0.68-0.75 everywhere, no sign reversals) is the qualitative change
from the V1.1 redesign — it was previously the least stable and often
negative. Updating recovery remains the most modest (r = 0.26-0.55).

### 2.5 Known limitations / open issues

- This is a first-pass sweep (one simulated replicate per condition), not a
  fully replicated Monte Carlo design with repeated-sampling variability
  estimated at each condition.
- Updating recovery, while now well-identified, remains only moderate. This
  may be a genuine property of the construct (limited independent signal once
  comprehension and evidence strength are accounted for) or may reflect that a
  single initial-judgment/correction/post-judgment cycle per item is still a
  thin design — worth testing with a richer item structure before concluding
  either way.
- All of the above is evidence about a synthetic, programmed data-generating
  process. None of it is evidence of construct validity in real people.

## 3. Roadmap: next steps based on psychometric research practice

Study 0 has done what a synthetic benchmark can do: it now shows the proposed
architecture is internally coherent for all five estimated dimensions, after
an iteration that fixed evidence-evaluation's initially weak, unstable
recovery. Standard practice for developing a
performance-based psychometric instrument (e.g., AERA/APA/NCME *Standards for
Educational and Psychological Testing*; COSMIN guidance for measurement
properties) points to the following next steps, in order:

### 3.1 Close out Study 0 (short-term, low-cost)

1. **Upgrade the Monte Carlo sweep to a real replicated design**: multiple
   seeds per condition to get a mean ± spread for each recovery correlation,
   not just a point estimate.
2. **Test whether a richer updating item structure improves updating recovery
   further** (e.g., multiple evidence rounds, or an explicit weak-then-strong
   evidence sequence) — updating recovery (r = 0.26-0.55) is now well-identified
   but still the most modest of the five dimensions.
3. ~~Resolve the data-provenance gap~~ and ~~redesign the evidence-evaluation
   measurement~~ — both done; see section 2.4 above.

### 3.2 Study 1 — item and instrument development (next major phase)

This is where standard instrument-development practice becomes the driver
rather than simulation engineering:

- **Literature synthesis**: a first-pass synthesis of existing instruments and
  paradigms (MIST, lateral reading, continued-influence-effect/backfire-effect
  research, illusory truth effect, "lazy not biased" sharing research) is
  drafted in [literature_review.md](literature_review.md), with citations flagged as needing
  verification against a real database before use in any external-facing
  document. This should be completed and verified before finalizing item
  content, since it identifies both the convergent-validity anchor (MIST) and
  the dimension least covered by existing instruments (evidence evaluation).
- **Content validity**: expert panel review of item pool against the construct
  definition; map every item to a dimension and record disagreements.
- **Cognitive interviewing / think-aloud pretesting** (typically n ≈ 10–20) to
  catch construct-irrelevant variance (confusing wording, unintended cues)
  before large-scale piloting.
- **Real claim sourcing**: replace abstract simulated item parameters with
  actual fact-checked claims (e.g., drawing on PolitiFact/Snopes-style corpora),
  with real difficulty/discrimination estimated empirically rather than assumed.
- **Preregistration** of the pilot analysis plan (e.g., via OSF): hypothesized
  factor structure, planned models, and stopping rules, given this program's
  own stated commitment to a measurement-first, blind-analysis logic.
- **IRB/ethics approval** for human-subjects data collection, and a data
  management/privacy plan for response and (if collected) demographic data.
- **Pilot sample size planning**: for IRT calibration of item parameters,
  conventional guidance suggests roughly 200–500 respondents per unidimensional
  item set (more for multidimensional models); for exploratory factor analysis,
  a minimum of ~300 or a 10:1 respondent-to-item ratio is a common rule of
  thumb. This should be formalized via a power analysis once item counts per
  dimension are finalized.

### 3.3 Study 2 — human validation and psychometrics

- Reliability: internal consistency (e.g., omega/alpha where appropriate for
  formative vs. reflective indicators) and test-retest stability.
- Factor structure: confirmatory factor analysis / multidimensional IRT testing
  whether discernment, calibration, evidence evaluation, updating,
  verification, and sharing restraint load as separable factors in real data
  (the key open question flagged by Study 0C).
- Measurement invariance across relevant subgroups (e.g., age, education,
  political orientation) before making group comparisons.
- Convergent/discriminant validity against existing instruments in the
  literature (e.g., Cognitive Reflection Test, News Literacy scales, existing
  misinformation-susceptibility measures) to situate the new instrument
  relative to prior work.
- Confidence calibration analysis using real accuracy data (Study 0 only
  simulated this).

### 3.4 Study 3 — predictive validity

- Test whether the validated measurement model predicts downstream behavior:
  actual sharing behavior, susceptibility to a novel misinformation exposure,
  or belief change following real corrective interventions.
- Longitudinal or experimental designs are preferable to cross-sectional
  self-report for this stage.

### 3.5 Study 4 — applied modeling and intervention support

- Use the validated instrument to identify who is most vulnerable and under
  what conditions, and evaluate decision-support or media-literacy
  interventions, ideally via randomized designs with the Study 2/3 measures as
  outcomes.

## 4. Bottom line

Study 0 is functionally complete for its intended scope: all seven proposed
dimensions now have a coherent measurement approach in simulation, with five of
them (discernment, response bias, verification, evidence evaluation, updating)
formally recoverable via item-level models, stably across a wide sensitivity
sweep. The evidence-evaluation gap flagged earlier in this report was closed
by making evidence comprehension an observable response rather than a hidden
latent — a concrete example of the research-practice principle that synthetic
benchmarks should be used to fail fast and iterate before human data
collection, not just to document a limitation. The responsible next step is
Study 1 item development, informed by the literature synthesis, with updating's
still-modest recovery flagged as the one dimension warranting a richer item
structure before finalizing content.
