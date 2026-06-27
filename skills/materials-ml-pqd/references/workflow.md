# Materials ML Workflow

## 1. Define the scientific question

Start by classifying the task:

- `regression`: PLQY, emission peak, FWHM, lifetime, stability retention, scintillation intensity, light yield, dose response.
- `classification`: phase stability, bright/dim sample, pass/fail synthesis, high/low stability, emission color class.
- `ranking`: prioritize candidate compositions or synthesis windows.
- `screening`: identify promising composition/ligand/shell/matrix conditions.
- `interpretability`: explain trends, feature effects, or descriptor-response relationships.

Always separate:
- prediction target,
- scientific claim,
- experimental decision,
- figure/reporting need.

## 2. Audit the data before modeling

Check:

- number of samples and features,
- missing values,
- duplicated samples,
- repeated papers or synthesis batches,
- near-identical compositions,
- inconsistent units,
- measurement conditions,
- target distribution,
- outliers and whether they are real or data-entry errors.

For literature datasets, record source paper, sample identifier, measurement method, and extraction notes.

## 3. Define leakage-safe splits

Potential leakage sources in materials ML:

- samples from the same paper split across train/test,
- same composition with minor ligand variations split across train/test,
- duplicate or near-duplicate measurements,
- target-derived features, such as using emission peak-derived color label to predict emission peak,
- post-treatment descriptors unavailable before synthesis.

Prefer:

- group split by `source_id`, `paper_id`, or `batch_id`,
- leave-one-family-out split for composition generalization,
- repeated K-fold only when grouping is not available and the limitation is stated.

## 4. Establish baselines

Before complex models, run:

- mean/median baseline,
- linear regression or ridge/elastic net,
- random forest,
- gradient boosting,
- Gaussian process for small data when uncertainty is useful.

A model is not meaningful unless it beats simple baselines under the same validation protocol.

## 5. Validate

Use metrics appropriate for the target:

Regression:
- MAE,
- RMSE,
- R2,
- Spearman/Pearson correlation,
- prediction interval coverage when uncertainty is reported.

Classification:
- balanced accuracy,
- F1 score,
- ROC-AUC or PR-AUC when appropriate,
- confusion matrix.

Small-data recommendation:
- repeated cross-validation,
- nested CV if hyperparameter tuning is extensive,
- bootstrap confidence intervals for metrics.

## 6. Interpret carefully

Use:

- permutation importance for model-agnostic ranking,
- SHAP for local/global contribution analysis,
- PDP/ICE for marginal effects,
- ablation tests for descriptor groups,
- domain checks to reject physically implausible explanations.

Never write: “SHAP proves the mechanism.”
Write instead: “The model associates feature X with the target under this dataset and validation protocol.”
