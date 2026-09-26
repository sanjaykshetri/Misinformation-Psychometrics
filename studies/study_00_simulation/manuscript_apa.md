Running head: MISINFORMATION VULNERABILITY SIMULATION BENCHMARK

# A Blind-Analysis Simulation Benchmark for Multidimensional Measurement of Misinformation Vulnerability

[Author Name]

[Affiliation]

## Author Note

This manuscript reports Study 0 of the Misinformation Psychometrics research
program: a fully synthetic, blind-analysis simulation benchmark. No human
participants, human data, or identifiable information were involved, and no
IRB/ethics review was required for this study. All simulated data, analysis
code, and results are available in the project repository
(`simulation/`, `data/simulated/`, `studies/study_00_simulation/`).

Several in-text citations below are drawn from the author's general
knowledge of the literature and have not yet been verified against a live
database (no literature-search access was available while drafting this
manuscript). Each such citation is marked **[VERIFY]** in the reference list
and must be confirmed against the original source before this manuscript is
submitted, published, or otherwise relied upon externally.

Correspondence concerning this article should be addressed to [Author Name],
[Email].

\newpage

## Abstract

Misinformation vulnerability is frequently operationalized as a single
accuracy score, a framing that conflates several plausibly separable
cognitive processes. We propose a seven-dimension construct (discernment,
response bias, confidence calibration, evidence evaluation, belief updating,
verification competence, and sharing restraint) and use a fully synthetic,
blind-analysis simulation to stress-test whether this architecture is
internally coherent before collecting human data. A data-generating model
produced responses for 1,000 simulated participants across 40 veracity items,
10 belief-updating items, and 10 verification items. Item-level models,
fit without access to the generating parameters, recovered discernment
(*r* = .927), verification ability (*r* = .816), and, after a design revision
described below, evidence-evaluation ability (*r* = .707); belief-updating
recovery was more modest (*r* = .383). An initial version of the
evidence-evaluation model relied on a hidden process variable folded into a
belief-movement score and recovered poorly and unstably (*r* = .133,
frequently sign-reversed across a 13-condition Monte Carlo robustness sweep).
Making evidence comprehension a directly observable, IRT-estimable response
resolved this, yielding stable recovery (*r* = .68–.75) across every
robustness condition tested. We discuss implications for instrument
development and outline a roadmap toward human item piloting.

*Keywords:* misinformation, psychometrics, simulation, Monte Carlo, item
response theory, construct validity

\newpage

## Introduction

### The Problem with Single-Score Misinformation Measures

Research on susceptibility to misinformation commonly reduces performance to
a single accuracy or discernment score across true and false claims. This is
a defensible starting point, but it risks conflating processes that may be
theoretically and practically distinct: a person's ability to discriminate
true from false claims is not the same quantity as their general tendency to
endorse claims as true, their confidence calibration, their capacity to
interpret corrective evidence, their tendency to revise judgments after such
evidence, their skill at active verification, or their restraint in sharing
unverified content (see `docs/construct_definition.md` in the accompanying
repository for the full construct definition used in this program).

A signal-detection reframing of "fake news detection" as a joint function of
sensitivity and criterion has previously been proposed as a way to separate
discernment from response bias **[VERIFY: Batailler, Brannon, Teas, & Gawronski, 2022]**,
and is one of the few points in this literature where the conventional
accuracy score has already been formally decomposed. Analytic-thinking
measures such as the Cognitive Reflection Test have been linked to fake-news
discernment **[VERIFY: Frederick, 2005; Pennycook & Rand, 2019]**, and an
inattention-based account of low-quality sharing behavior has been proposed
as an alternative to motivated-reasoning accounts **[VERIFY: Pennycook & Rand, 2019]**.
Belief-revision failures following correction have been studied under the
label of the continued influence effect **[VERIFY: Johnson & Seifert, 1994;
Lewandowsky, Ecker, Seifert, Schwarz, & Cook, 2012]**, and claims about a
reliable "backfire effect" in which corrections increase belief in
misinformation have more recently been challenged **[VERIFY: Wood & Porter, 2019]**.
Verification skill has been studied through the lens of lateral reading,
contrasting how novices and fact-checkers evaluate unfamiliar online sources
**[VERIFY: Wineburg & McGrew, 2019]**. A validated multidimensional composite
instrument, the Misinformation Susceptibility Test, has recently been
proposed as a convergent-validity anchor for this space **[VERIFY: Maertens
et al., 2024]**. Each of these traditions targets one or two of the seven
proposed dimensions; to our knowledge, no existing published instrument
attempts to measure all seven simultaneously with an explicit blind
recovery test of whether they are separable at all.

### The Present Study

Before collecting human data, we used a synthetic benchmark to ask a
narrower, prior question: if a data-generating process were constructed to
instantiate all seven dimensions as at least partially independent latent
traits, could conventional psychometric methods recover them from observed
task responses alone, without ever consulting the generating parameters
during model development? We refer to this as Study 0, and to the underlying
logic as a *blind-analysis* workflow: item-level models are fit exclusively
from observed responses, and the hidden generating traits are loaded only
afterward, for a one-time post-estimation comparison.

Study 0 has three parts. Study 0A computes observed-only descriptive summary
scores. Study 0B fits explicit item-level statistical models (rather than
relying on summary scores) to estimate person parameters for discernment,
response bias, verification ability, evidence-evaluation ability, and belief
updating. Study 0C repeats the Study 0B models on newly simulated datasets
that each vary one data-generating condition (sample size, item count, item
difficulty spread, response noise, carelessness rate, or latent correlation
strength) away from a baseline, to test whether recovery is an artifact of
one convenient parameter setting.

We report two versions of the evidence-evaluation model. The first version
(V1) inferred evidence-evaluation ability only indirectly, as a random slope
in a model of belief movement. Because this recovered evidence-evaluation
poorly and unstably, we redesigned the measurement (V1.1) so that evidence
comprehension is a directly observable, binary comprehension-check response,
modeled the same way as the verification task. We report both versions here
because the contrast is itself a methodological finding: a synthetic
benchmark can reveal that a construct is unrecoverable *because of a fixable
measurement-design flaw*, not because the construct is inherently
inseparable from its neighbors — and that this can be diagnosed and repaired
before, rather than after, expensive human data collection.

## Method

### Design Overview

This is a Monte Carlo simulation study with three linked analyses (Study 0A,
0B, 0C), not a study of human participants. All data were generated by a
known, documented stochastic process (`simulation/SIMULATION_SPEC_V1.md`),
which allows the "ground truth" latent traits to be compared against
estimates obtained without reference to them.

### Simulated Sample and Item Bank

The baseline dataset comprised 1,000 simulated participants. Each participant
completed 40 veracity-judgment items (half true, half false claims), 10
belief-updating items (an initial judgment, corrective evidence, and a
post-correction judgment), and 10 verification items (choosing an effective
verification action). Item parameters (difficulty, discrimination, topic,
emotionality, political valence, source credibility, linguistic
plausibility, prior-exposure rate, and, for updating items, evidence
strength and evidence complexity) were themselves randomly generated per
item from documented distributions.

### Data-Generating Model

Ten correlated latent participant traits were drawn from a multivariate
normal distribution with a fixed correlation structure: discernment,
calibration, evidence evaluation, updating, verification, sharing restraint,
general knowledge, credulity bias, congruence susceptibility, and emotional
reactivity, plus an independently distributed carelessness probability.
Observed responses (veracity judgments, confidence ratings, sharing
decisions, updating judgments, comprehension-check responses, and
verification choices) were generated as logistic or probability-threshold
functions of these traits and the corresponding item parameters, with
additive noise and a per-trial probability of careless (near-random)
responding. Full generating equations are documented in
`simulation/SIMULATION_SPEC_V1.md`.

**The V1.1 revision.** In the original design, evidence comprehension was
represented only as a hidden latent variable folded directly into the
belief-movement calculation; it was not a response a real assessment could
ever observe. We revised the model so that participants instead emit an
observable binary response, `comprehension_correct`, drawn from a Bernoulli
distribution whose probability is a logistic function of evidence-evaluation
ability, item evidence-complexity, and general knowledge. Belief movement
continues to depend on the same underlying continuous comprehension signal
(not the binarized response itself, which is a noisy indicator of it), so
that the belief-updating process is unchanged in its qualitative structure
while evidence comprehension becomes independently measurable.

### Analytic Strategy

**Study 0A (observed-only descriptive benchmark).** Participant-level summary
scores (overall and conditional accuracy, signal-detection *d′* and
criterion, mean confidence, confidence–accuracy gap, Brier score, share
rate, sharing-restraint score, updating success rate, mean appropriate
belief movement, and verification accuracy) were computed from the observed
response files only.

**Study 0B (item-level recovery models).** Four models were fit, in each
case using only observed responses:

1. *Veracity model.* For each participant, a two-parameter logistic model
   (response-bias intercept and truth-status-weighted discernment slope) was
   fit by penalized maximum likelihood across that participant's 40 veracity
   judgments.
2. *Verification model.* A person–item (Rasch-style) logistic model was fit
   across all participants' binary verification-item outcomes, using
   item-level correct-response rates as fixed item difficulties and
   estimating a person ability parameter per participant.
3. *Evidence-comprehension model.* The same person–item logistic approach was
   applied to the observed `comprehension_correct` responses from the
   updating task, yielding an evidence-evaluation ability estimate per
   participant.
4. *Updating model.* A two-level (mixed-effects) linear model of
   appropriate belief movement was fit with evidence strength (item-level)
   and the *within-person* deviation of `comprehension_correct` as fixed
   effects and a random intercept per participant. The within-person
   centering was necessary because comprehension and updating are
   correlated traits in the generating model; an initial specification using
   the raw (uncentered) response as a single fixed effect conflated the two,
   suppressing the updating estimate (see Results).

**Study 0C (Monte Carlo robustness sweep).** All four Study 0B models were
re-fit on 13 freshly simulated datasets, each varying exactly one
generating condition away from the baseline: sample size (250, 1,000, 2,000),
veracity item count (20, 40, 80), item difficulty spread (narrower, baseline,
wider), response noise (lower, baseline, higher), carelessness rate (lower,
baseline, higher), and latent correlation strength (weaker, moderately
weaker, baseline). This is a one-factor-at-a-time sensitivity sweep rather
than a fully replicated design with repeated-sampling variability estimated
at each condition.

In all cases, the hidden generating traits (`participants.csv`) were loaded
only after model fitting, for a single post-estimation Pearson correlation
between each estimated quantity and its intended hidden trait.

## Results

### Descriptive Benchmark (Study 0A)

The baseline synthetic sample showed a broad, interpretable range of
simulated behavior: mean veracity accuracy = .605, mean confidence = 83.31
(0–100 scale), share rate = .419, careless-trial rate = .057, updating
success rate = .764, and verification accuracy = .440.

### Item-Level Recovery (Study 0B)

Table 1 reports the correlation between each item-level model's estimate and
its intended hidden generating trait on the baseline dataset. Discernment
(*r* = .927), verification ability (*r* = .816), and evidence-evaluation
ability (*r* = .707) were recovered strongly; response bias was recovered
moderately (*r* = .549); belief updating was recovered modestly
(*r* = .383).

*Table 1*

*Item-Level Recovery Correlations, Baseline Dataset*

| Model | Estimated quantity | Hidden trait | *r* |
|---|---|---|---|
| Veracity (person-level MLE) | Discernment | Discernment | .927 |
| Veracity (person-level MLE) | Response bias | Credulity bias | .549 |
| Verification (person–item IRT) | Verification ability | Verification | .816 |
| Evidence comprehension (person–item IRT) | Evidence-evaluation ability | Evidence evaluation | .707 |
| Updating (two-level model) | Updating ability | Updating | .383 |

*Note.* Evidence-evaluation recovery reflects the V1.1 design, described
above. An earlier version, in which evidence-evaluation ability was inferred
only as a random slope in the updating model without an observable
comprehension response, recovered evidence evaluation at *r* = .133. A
first attempt at the V1.1 updating model, which entered the raw
(non-centered) `comprehension_correct` response as a shared fixed effect,
recovered updating at only *r* = .165, because comprehension and updating
are correlated traits (population *r* = .52 in the generating model) and the
shared slope absorbed between-person variance that belonged to the updating
estimate. Within-person centering of the comprehension predictor, reported
in Table 1, restored updating recovery to the level obtained by the original
design (*r* = .383 vs. .374).

### Monte Carlo Robustness (Study 0C)

Table 2 summarizes recovery across the 13 sweep conditions. Discernment
(range = .871–.936), response bias (range = .490–.571), and verification
(range = .778–.843) recovery were stable in both sign and approximate
magnitude across every condition. Updating recovery was more variable
(range = .264–.551) but never fell to zero or reversed sign. Evidence-
evaluation recovery under the V1.1 design was stable and strong everywhere
tested (range = .684–.748); the same sweep applied to the earlier V1 design
had produced negative correlations in 8 of 12 non-baseline conditions
(range = −.231 to .228), which we interpret as a measurement-architecture
failure rather than evidence that the dimension is inherently
unmeasurable.

*Table 2*

*Monte Carlo Robustness Sweep (V1.1 Design)*

| Condition | Discernment *r* | Response-bias *r* | Verification *r* | Updating *r* | Evidence-evaluation *r* |
|---|---|---|---|---|---|
| Baseline (*N* = 1,000, 40 items) | .927 | .549 | .816 | .383 | .707 |
| *N* = 250 | .913 | .507 | .832 | .382 | .708 |
| *N* = 2,000 | .917 | .525 | .815 | .357 | .736 |
| 20 veracity items | .891 | .538 | .828 | .382 | .697 |
| 80 veracity items | .933 | .548 | .795 | .441 | .720 |
| Narrower item difficulty | .907 | .571 | .836 | .338 | .740 |
| Wider item difficulty | .927 | .551 | .811 | .551 | .721 |
| Lower response noise | .899 | .531 | .834 | .264 | .736 |
| Higher response noise | .914 | .497 | .836 | .438 | .717 |
| Lower carelessness | .936 | .543 | .843 | .423 | .748 |
| Higher carelessness | .871 | .490 | .785 | .398 | .684 |
| Weaker latent correlation | .901 | .550 | .778 | .392 | .710 |
| Moderately weaker latent correlation | .909 | .562 | .810 | .394 | .713 |

*Note.* Full results, including the corresponding V1 (pre-redesign) sweep,
are available in `studies/study_00_simulation/monte_carlo_results.csv` and
`docs/project_status.md`.

## Discussion

### Principal Findings

Five of seven proposed dimensions now have a working item-level measurement
approach that recovers the intended hidden trait with reasonable to strong
accuracy, stably across a range of sample sizes, item counts, item
difficulties, response noise levels, carelessness rates, and latent
correlation strengths. Discernment, verification competence, and (after
redesign) evidence-evaluation ability were the most strongly and stably
recovered. Response bias and belief updating were recovered less strongly
but not unstably.

### The Evidence-Evaluation Case Study

The most informative result in this study is arguably the contrast between
the V1 and V1.1 evidence-evaluation models rather than either result in
isolation. In V1, evidence comprehension existed only as an internal process
variable that the belief-movement calculation used but never exposed as an
observable response — essentially, no real assessment could ever have
measured it, because it was never something a participant did or said. Its
poor, sign-unstable recovery could easily have been (mis)read as evidence
that evidence-evaluation ability is not a coherent, separable construct.
Once evidence comprehension was operationalized as an explicit, observable
comprehension-check response and modeled the same way verification ability
already was, recovery became strong and stable. This suggests that at least
some of the difficulty other researchers have had in operationalizing
evidence-evaluation or evidence-interpretation constructs may be a
measurement-design problem rather than a construct-validity problem, though
this synthetic result cannot by itself establish which explanation applies
to real human data.

A related methodological finding concerns the updating model. Because
comprehension and updating are correlated in the generating model,
entering the raw per-trial comprehension response as a single fixed effect
in the belief-movement model suppressed the updating estimate — a
within/between-cluster conflation familiar from the multilevel-modeling
literature. Group-mean centering the comprehension predictor (a Mundlak-style
decomposition) resolved this. We flag this because the same conflation risk
will apply directly to any future human study that measures comprehension
and updating from the same items.

### Limitations

This is a synthetic, programmed data-generating process; none of these
results are evidence of construct validity in real people, and none of the
correlations reported here should be interpreted as effect sizes expected in
human data. The Monte Carlo sweep is a one-factor-at-a-time design with a
single simulated replicate per condition, not a fully replicated design with
repeated-sampling variability estimated at each condition. Updating recovery
remains the most modest of the five dimensions; whether this reflects a
genuine ceiling on how much independent signal belief-revision quality
carries once comprehension and evidence strength are accounted for, or
whether it reflects that a single initial-judgment/correction/post-judgment
cycle per item is a thin design, cannot be determined from this study alone.

### Future Directions

The logical next step is human item development (Study 1), informed by a
still-to-be-verified literature synthesis (`docs/literature_review.md`) that
identifies the Misinformation Susceptibility Test as the primary existing
convergent-validity anchor and the lateral-reading and continued-
influence-effect literatures as templates for verification and updating item
design, respectively. Subsequent stages (Study 2: human psychometric
validation; Study 3: predictive validity; Study 4: applied/intervention
work) are outlined in `docs/research_roadmap.md` and `docs/project_status.md`.

### Conclusion

A fully synthetic, blind-analysis benchmark showed that five proposed
dimensions of misinformation vulnerability — discernment, response bias,
verification competence, evidence-evaluation ability, and belief updating —
can be recovered from simulated behavioral responses using item-level
statistical models, and that this recovery is stable across a range of
sample sizes and data-generating conditions. The initially poor recovery of
evidence-evaluation ability was traced to a specific, fixable flaw in how
that construct was operationalized, rather than to the construct itself, and
was resolved by making evidence comprehension a directly observable response.
This benchmark does not establish construct validity in humans, but it
provides methodological justification, and a documented set of design
lessons, for proceeding to human item development.

\newpage

## References

*The following entries are drawn from the author's general domain knowledge
and are marked [VERIFY]; each must be confirmed against the original source
before this reference list is relied upon externally.*

American Educational Research Association, American Psychological
Association, & National Council on Measurement in Education. (2014).
*Standards for educational and psychological testing*. American Educational
Research Association. **[VERIFY]**

Batailler, C., Brannon, S. M., Teas, P. E., & Gawronski, B. (2022). A signal
detection approach to understanding the identification of fake news.
*Perspectives on Psychological Science*, *17*(1), 78–98. **[VERIFY]**

Frederick, S. (2005). Cognitive reflection and decision making. *Journal of
Economic Perspectives*, *19*(4), 25–42. **[VERIFY]**

Johnson, H. M., & Seifert, C. M. (1994). Sources of the continued influence
effect: When misinformation in memory affects later inferences. *Journal of
Experimental Psychology: Learning, Memory, and Cognition*, *20*(6),
1420–1436. **[VERIFY]**

Lewandowsky, S., Ecker, U. K. H., Seifert, C. M., Schwarz, N., & Cook, J.
(2012). Misinformation and its correction: Continued influence and
successful debiasing. *Psychological Science in the Public Interest*,
*13*(3), 106–131. **[VERIFY]**

Maertens, R., Götz, F. M., Golino, H. F., Roozenbeek, J., Schneider, C. R.,
Kyrychenko, Y., Kerr, J. R., Stieger, S., McClanahan, W. P., Drobnjak, J.,
Basol, M., Uenal, F., Rathje, S., & van der Linden, S. (2024). The
Misinformation Susceptibility Test (MIST): A psychometrically validated
measure of news veracity discernment. *Behavior Research Methods*, *56*(3),
1863–1899. **[VERIFY]**

Pennycook, G., Epstein, Z., Mosleh, M., Arechar, A. A., Eckles, D., & Rand,
D. G. (2021). Shifting attention to accuracy can reduce misinformation
online. *Nature*, *592*(7855), 590–595. **[VERIFY]**

Pennycook, G., & Rand, D. G. (2019). Lazy, not biased: Susceptibility to
partisan fake news is better explained by lack of reasoning than by
motivated reasoning. *Cognition*, *188*, 39–50. **[VERIFY]**

Pennycook, G., Cheyne, J. A., Barr, N., Fugelsang, J. A., & Koehler, D. J.
(2015). On the reception and detection of pseudo-profound bullshit.
*Judgment and Decision Making*, *10*(6), 549–563. **[VERIFY]**

Wineburg, S., & McGrew, S. (2019). Lateral reading and the nature of
expertise: Reading less and learning more when evaluating digital
information. *Teachers College Record*, *121*(11), 1–40. **[VERIFY]**

Wood, T., & Porter, E. (2019). The elusive backfire effect: Mass attitudes'
steadfast factual adherence. *Political Behavior*, *41*(1), 135–163.
**[VERIFY]**
