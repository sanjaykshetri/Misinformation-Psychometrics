# Misinformation Psychometrics

Misinformation Psychometrics is an open research program for conceptualizing, measuring, and modeling individual differences in vulnerability to misinformation.

This project treats misinformation vulnerability as a multidimensional construct rather than a single trait. The central scientific question is whether people vary systematically in:

- their ability to discriminate true from false claims,
- their response bias toward endorsing claims as true,
- their confidence calibration,
- their capacity to evaluate evidence,
- their ability to update beliefs after corrective information,
- their verification competence,
- and their willingness to share content without sufficient checking.

The repository is designed as a research program, with a synthetic simulation serving as a pilot benchmark for measurement recovery and psychometric analysis.

## Research problem

Misinformation vulnerability is not well captured by a single "fake-news score." In practice, the phenomenon likely combines at least:

- veracity discernment,
- uncertainty calibration,
- evidence evaluation,
- belief updating,
- verification skill,
- sharing restraint,
- and susceptibility to contextual distortions such as congruence or emotionality.

The project asks whether these dimensions can be measured in a way that is theoretically coherent, empirically recoverable, and psychometrically useful.

## Conceptual model

A useful measurement model for misinformation vulnerability should separate three broad families of effects:

1. Signal detection and factual discrimination
2. Decision bias and confidence calibration
3. Evidence-informed reasoning and verification behavior

This is the motivation behind the simulation in Study 0: to test whether a theoretically specified multidimensional data-generating process can be recovered from observed behavior without using the generating parameters directly.

## Research program

The project is organized around staged research questions:

- Study 0: synthetic benchmark and recovery analysis
- Study 1: item development and pilot measurement design
- Study 2: psychometric validation in human samples
- Study 3: construct refinement and predictive validity
- Study 4: applied intervention and decision-support modeling

## Current study: Study 0

Study 0 is a synthetic data exercise designed to evaluate whether psychometric methods can recover known dimensions from observed response patterns alone.

The key methodological boundary is intentionally strict:

DATA-GENERATING MODEL
    ↓
participants.csv
(true latent parameters)
    ↓
      HIDDEN
────────────────────────
    ↓
Observed responses only
    ↓
Psychometric analysis
    ↓
Estimated traits
    ↓
────────────────────────
    ↓
Compare estimates with
known simulated truth

This is a blind-analysis benchmark. We do not use the latent generating variables directly when fitting the model. Only after estimation do we reveal the generating parameters to evaluate recovery.

The principal question for Study 0 is:

> Given a theoretically specified multidimensional data-generating process, to what extent can conventional psychometric methods recover the simulated dimensions of misinformation vulnerability from observed assessment responses?

## Repository structure

- [README.md](README.md): project overview and scientific framing
- [requirements.txt](requirements.txt): Python environment for analysis
- [.gitignore](.gitignore): standard ignore rules for notebooks and virtual environments
- [docs/construct_definition.md](docs/construct_definition.md): conceptual definition of misinformation vulnerability dimensions
- [docs/research_roadmap.md](docs/research_roadmap.md): planned research agenda
- [docs/project_status.md](docs/project_status.md): current status report and next-step roadmap grounded in psychometric research practice
- [docs/literature_review.md](docs/literature_review.md): synthesis of existing research relevant to misinformation vulnerability measurement (unverified citations, flagged for follow-up)
- [simulation/](simulation/): synthetic data generator, specification, and sanity checks
- [data/simulated/](data/simulated/): generated CSV outputs used for analysis
- [notebooks/01_simulation_eda.ipynb](notebooks/01_simulation_eda.ipynb): observed-only Study 0A exploratory analysis
- [studies/study_00_simulation/README.md](studies/study_00_simulation/README.md): blind-analysis guide for the simulated benchmark
- [studies/study_00_simulation/model_recovery.py](studies/study_00_simulation/model_recovery.py): item-level Study 0B recovery models (veracity, verification, updating, and evidence comprehension)
- [studies/study_00_simulation/study_00c_monte_carlo.py](studies/study_00_simulation/study_00c_monte_carlo.py): Study 0C Monte Carlo robustness sweep across data-generating conditions

## Data and simulation files

The data in this repository are methodological scaffolding for testing measurement and recovery, not evidence that the final construct is established.

- [simulation/SIMULATION_SPEC_V1.md](simulation/SIMULATION_SPEC_V1.md): specification for the synthetic data-generating model
- [simulation/simulate_misinformation_vulnerability_v1.py](simulation/simulate_misinformation_vulnerability_v1.py): script that generates synthetic responses
- [simulation/SANITY_CHECKS.txt](simulation/SANITY_CHECKS.txt): baseline diagnostics on the generated data
- [data/simulated/participants.csv](data/simulated/participants.csv): hidden generating parameters for the simulated sample
- [data/simulated/items.csv](data/simulated/items.csv): item parameters and module metadata
- [data/simulated/veracity_responses.csv](data/simulated/veracity_responses.csv): veracity judgments and confidence data
- [data/simulated/updating_responses.csv](data/simulated/updating_responses.csv): belief-updating task responses
- [data/simulated/verification_responses.csv](data/simulated/verification_responses.csv): verification-task responses
- [data/simulated/scale_scores.csv](data/simulated/scale_scores.csv): participant-level summary scores
- [data/simulated/observed_participant_summary.csv](data/simulated/observed_participant_summary.csv): observed-only estimates produced by Study 0A

## Reproducibility

To run the simulation and explore the generated data:

1. Create a Python environment and install dependencies from [requirements.txt](requirements.txt).
2. Run the simulation script: python simulation/simulate_misinformation_vulnerability_v1.py
3. Review the sanity checks in [simulation/SANITY_CHECKS.txt](simulation/SANITY_CHECKS.txt).
4. Open [notebooks/01_simulation_eda.ipynb](notebooks/01_simulation_eda.ipynb) for the observed-only Study 0A workflow.
5. Run `python studies/study_00_simulation/model_recovery.py` for the item-level Study 0B benchmark and post-estimation recovery comparison.
6. Run `python studies/study_00_simulation/study_00c_monte_carlo.py` for the Study 0C Monte Carlo robustness sweep across sample size, item count, difficulty, noise, carelessness, and latent correlation conditions.

Important: the synthetic data are useful for methodological stress testing, but they are not a substitute for human measurement validation.

---

This repository is intentionally structured as a research program rather than a single one-off script. The project aims to evolve from synthetic construct recovery toward a defensible psychometric model of misinformation vulnerability.
