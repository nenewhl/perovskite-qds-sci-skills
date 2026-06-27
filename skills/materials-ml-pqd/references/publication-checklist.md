# Publication Checklist for Materials ML PQD Work

## Dataset reporting

Report:

- number of samples,
- number of sources or batches,
- target variable definition,
- descriptor list,
- missing-value treatment,
- unit conversions,
- duplicate handling,
- train/validation/test split protocol,
- code and data availability where possible.

## Model reporting

Report:

- baseline model performance,
- selected model and hyperparameters,
- validation strategy,
- metric mean and uncertainty,
- random seed policy,
- external test results if available.

## Claim control

Do not overstate prediction accuracy or mechanism.

Safe claim structure:

1. Dataset scope.
2. Model task.
3. Validation protocol.
4. Performance with uncertainty.
5. Interpretation limited to learned associations.
6. Experimental follow-up needed.

## Reviewer risk points

Reviewers often question:

- small dataset size,
- literature extraction bias,
- train/test leakage,
- missing negative results,
- inconsistent measurement conditions,
- overuse of SHAP as mechanism proof,
- lack of external validation,
- no baseline comparison,
- unclear descriptor availability before synthesis.

Prepare responses before submission.
