# Misinformation Vulnerability Simulation V1

This folder contains a theory-driven synthetic-data generator for pretesting a proposed
multidimensional assessment of misinformation vulnerability.

## Start here

1. Read `SIMULATION_SPEC_V1.md`.
2. Run `simulate_misinformation_vulnerability_v1.py`.
3. Inspect `SANITY_CHECKS.txt`.
4. Analyze the generated CSV files.

## Main files

- `participants.csv`: known ("true") participant latent traits.
- `items.csv`: known item parameters.
- `veracity_responses.csv`: initial truth judgments, confidence, sharing, exposure, and response time.
- `updating_responses.csv`: pre/post-evidence judgments and appropriate belief movement.
- `verification_responses.csv`: verification-task performance.
- `scale_scores.csv`: observable participant-level summary scores.

The most important feature of simulation is that `participants.csv` contains the latent
traits used to generate responses. This lets us test whether an analysis applied only to
the observed responses can recover those known traits.

These synthetic results are engineering checks, not psychometric validation evidence.
