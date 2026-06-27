---
name: materials-ml-pqd
description: Materials-science machine-learning skill focused on perovskite quantum dots and nanocrystals. Use when the user asks for 材料机器学习, 钙钛矿量子点机器学习, PQD ML, perovskite QD prediction, SHAP, GAM, feature engineering, PLQY prediction, emission wavelength prediction, stability prediction, synthesis optimization, interpretable ML for luminescent materials, or publication-grade ML workflow for materials datasets.
---

# Materials ML PQD Skill

Use this skill for materials-science machine learning, especially perovskite quantum dots (PQDs), nanocrystals, scintillators, luminescent materials, and small-sample scientific datasets.

This skill is not a black-box prediction shortcut. It should enforce data integrity, leakage control, physically meaningful descriptors, transparent validation, and mechanism-aware interpretation.

## Trigger scenarios

Use this skill when the request involves:

- Building a machine-learning workflow for perovskite quantum dots or nanocrystals.
- Predicting or analyzing PLQY, emission peak, FWHM, lifetime, stability, scintillation response, light yield, X-ray response, film performance, or synthesis outcome.
- Designing descriptors/features for CsPbX3, FAPbX3, MAPbX3, mixed-halide PQDs, doped PQDs, shell-coated PQDs, ligand-engineered PQDs, or PQD-polymer films.
- Generating SHAP, PDP, ICE, permutation importance, feature-ablation, GAM-like dependence plots, or model interpretation figures.
- Comparing models such as linear baseline, random forest, XGBoost/LightGBM, Gaussian process regression, support vector regression, elastic net, or ensemble models.
- Preparing ML figures or methods sections for SCI manuscripts, dissertations, project reports, or group meetings.

## Required reading order

1. Read `references/workflow.md` for the overall task protocol.
2. Read `references/data-standards.md` before touching a dataset.
3. Read `references/pqd-feature-engineering.md` for PQD descriptors and domain constraints.
4. Read `references/modeling-and-validation.md` before model training or metric reporting.
5. Read `references/interpretability-and-figures.md` before SHAP/PDP/figure generation.
6. Read `references/publication-checklist.md` before writing claims, captions, methods, or reviewer-facing summaries.

## Core principles

- Never invent data, citations, labels, model scores, or mechanisms.
- Treat every ML result as conditional on dataset size, sampling bias, descriptor quality, and validation strategy.
- For small materials datasets, prioritize robust baselines, repeated cross-validation, and uncertainty over aggressive model complexity.
- Avoid leakage: do not let the same paper, synthesis batch, composition family, or near-duplicate sample appear in both train and test when that would inflate performance.
- Separate correlation, model importance, and physical mechanism. SHAP or feature importance is not proof of mechanism.
- For PQDs, interpret ML outputs through composition, ionic structure, surface chemistry, synthesis, passivation, shell/matrix effects, and measurement conditions.

## Output contract

For substantial tasks, return:

1. Detected ML objective and target variable.
2. Dataset audit: rows, columns, missingness, duplicates, units, leakage risk, and data-source bias.
3. Descriptor plan: raw features, engineered descriptors, excluded features, and reason.
4. Modeling plan: baseline, candidate models, validation split, metrics, and uncertainty.
5. Interpretation plan: SHAP/PDP/ICE/permutation/ablation as appropriate.
6. Publication-grade outputs: cleaned tables, reproducible scripts, figures, and cautious claims.
7. Limitations and next data needed.

## Default template files

- `templates/python/pqd_ml_pipeline.py`: end-to-end ML template.
- `templates/python/pqd_interpretability_template.py`: SHAP/PDP/permutation-importance plotting template.
- `templates/data/pqd_ml_example.csv`: synthetic example data for testing the workflow.
