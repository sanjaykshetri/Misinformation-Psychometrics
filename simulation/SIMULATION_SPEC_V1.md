# Misinformation Vulnerability Assessment — Simulation Specification V1

## Purpose

This simulation is a pre-data-collection stress test for a proposed multidimensional
performance-based assessment of misinformation vulnerability.

The simulation is NOT evidence that the proposed construct or factor structure exists in
humans. Its purpose is to test whether the proposed assessment architecture, scoring rules,
and analysis pipeline behave sensibly under known data-generating conditions.

## V1 research questions

1. Can observed responses recover an underlying discernment trait?
2. Can discernment be separated from a general true/false response bias?
3. Does confidence calibration contain information beyond raw accuracy?
4. Can evidence-updating performance be distinguished from initial discernment?
5. Can verification competence be distinguished from both discernment and updating?
6. Can sharing restraint vary independently enough to justify separate measurement?
7. How strongly do prior exposure and topic knowledge distort apparent performance?
8. How much do careless responders degrade measurement quality?

## Simulated sample

Default N = 1,000 simulated participants.

Participant latent characteristics:

- discernment: ability to distinguish true from false claims
- credulity_bias: tendency to judge claims as true regardless of truth status
- calibration: tendency for confidence to track decision quality
- evidence_evaluation: ability to interpret evidence quality
- updating: ability to revise judgments appropriately after corrective evidence
- verification: ability to select effective verification actions
- sharing_restraint: tendency to avoid sharing weak/uncertain claims
- general_knowledge: broad background knowledge
- congruence_susceptibility: extent to which identity/political congruence distorts judgment
- emotional_reactivity: extent to which emotionally provocative content distorts judgment
- carelessness: probability of inattentive/random responding

Core latent traits are generated from a correlated multivariate normal distribution.

## Simulated item bank

V1 contains:

- 40 veracity items (20 true, 20 false)
- 10 evidence-updating scenarios
- 10 verification-choice items

Veracity item properties:

- truth status
- difficulty
- discrimination
- topic
- knowledge demand
- emotionality
- political/identity valence
- source credibility
- linguistic plausibility
- prior-exposure base rate

Updating item properties:

- initial claim difficulty
- corrective evidence strength
- evidence complexity
- emotionality

Verification item properties:

- task difficulty
- discrimination
- topic

## Response-generating logic

### Veracity judgments

Each participant-item encounter creates a latent decision score.

For item j and participant i:

decision_ij =
    a_j * (
        truth_sign_j * discernment_i
        + truth_sign_j * knowledge_effect_ij
        - truth_sign_j * difficulty_j
        + credulity_bias_i
        + source_cue_effect_ij
        + plausibility_effect_ij
        + congruence_distortion_ij
        + emotional_distortion_ij
    )
    + random_error

truth_sign = +1 for true items and -1 for false items.

The observed response is TRUE if decision_ij > 0 and FALSE otherwise.

The response bias term does not reverse with truth status. Therefore a strongly positive
credulity_bias increases "true" responses for both true and false items.

### Prior exposure

Exposure probability varies by item. Exposure can help when the participant has adequate
knowledge, but it can also increase familiarity. V1 implements a modest net accuracy benefit
from exposure moderated by general knowledge.

### Confidence

Confidence depends on:

- absolute decision strength
- participant calibration
- correctness
- random noise

The simulation allows high-confidence errors and poorly calibrated respondents.

### Evidence updating

Participants first make an initial judgment. They then receive corrective evidence.
Movement toward the evidence-supported answer depends on:

- updating latent trait
- evidence-evaluation ability
- evidence strength
- evidence complexity
- emotional reactivity
- random error

### Verification

Probability of choosing the best verification action follows a logistic IRT-like function
of verification ability, item discrimination, and item difficulty.

### Sharing

Sharing probability depends on:

- perceived truth
- confidence
- item emotionality
- participant sharing restraint
- congruence susceptibility

This permits participants who are reasonably accurate but prone to sharing provocative or
uncertain content.

### Careless responding

Participants have individual carelessness probabilities. On a careless trial, responses
may be random, confidence becomes weakly informative, and response times become shorter.

## Output files

### participants.csv
One row per simulated participant containing latent characteristics.

### items.csv
One row per item containing item parameters and module membership.

### veracity_responses.csv
One row per participant × veracity item.

### updating_responses.csv
One row per participant × updating item.

### verification_responses.csv
One row per participant × verification item.

### scale_scores.csv
One row per participant with observable summary scores.

## Primary observable scores

- overall veracity accuracy
- true-item accuracy
- false-item accuracy
- signal-detection d-prime
- signal-detection criterion
- mean confidence
- confidence-accuracy gap
- Brier score
- updating success rate
- mean appropriate belief movement
- verification accuracy
- sharing restraint score

## Important V1 limitations

- Parameters are theory-informed but not fitted to human pilot data.
- Demographic variables are intentionally omitted from causal response generation in V1.
- Political congruence is abstract rather than tied to real parties or issues.
- No natural-language claim content is generated yet.
- The V1 generator does not fit a formal multidimensional model; initial item-level recovery models are documented separately in Study 0B.
- Simulated reliability and validity statistics are engineering checks, not empirical evidence.

## Recommended V2 extensions

1. Add explicit respondent profiles / mixture classes.
2. Add test-retest occasions.
3. Add multidimensional IRT estimation.
4. Add DIF simulations.
5. Vary sample size and test length through Monte Carlo replications.
6. Add missingness and speeded responding.
7. Add realistic natural-language item stems after construct review.
8. Fit simulation parameters to empirical pilot data once human data become available.