# Modeling and Validation Guide

## Recommended model ladder

Use a model ladder instead of jumping directly to complex algorithms:

1. Dummy baseline: mean/median prediction.
2. Linear baseline: ridge, lasso, elastic net.
3. Tree baseline: random forest.
4. Gradient boosting: XGBoost, LightGBM, HistGradientBoosting when available.
5. Gaussian process regression for small datasets and uncertainty.
6. SVR for small-to-medium tabular data.
7. Ensemble or stacking only after simple models are documented.

## Validation strategies

Choose validation based on the scientific question:

- Random split: only for preliminary exploration.
- GroupKFold by `source_id`: literature generalization.
- GroupKFold by `batch_id`: experimental batch generalization.
- Leave-one-composition-family-out: composition extrapolation.
- Time split: when using chronological experimental campaigns.
- External test set: best when available.

## Metrics

Regression:
- MAE for intuitive absolute error,
- RMSE for large-error sensitivity,
- R2 only when sample size and distribution justify it,
- Spearman correlation for ranking behavior,
- calibration and interval coverage for uncertainty models.

Classification:
- balanced accuracy,
- precision, recall, F1,
- ROC-AUC or PR-AUC,
- confusion matrix.

## Hyperparameter tuning

Use:

- simple grids or randomized search,
- nested CV for honest model selection when feasible,
- fixed random seeds,
- versioned train/test indices.

Avoid:

- tuning on the test set,
- reporting only the best random seed,
- comparing models under different splits,
- using too many hyperparameters for tiny datasets.

## Small-data principles

For materials datasets under a few hundred rows:

- limit feature count,
- prefer interpretable descriptors,
- use regularization,
- report uncertainty,
- use grouped validation,
- avoid overclaiming predictive power.
