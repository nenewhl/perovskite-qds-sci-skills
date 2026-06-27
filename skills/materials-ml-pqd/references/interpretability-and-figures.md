# Interpretability and Figure Guide

## Recommended interpretation stack

Use multiple checks:

1. Permutation importance for model-agnostic feature ranking.
2. SHAP summary plot for global contribution patterns.
3. SHAP dependence plot for high-impact features.
4. PDP/ICE for marginal effect visualization.
5. Feature-group ablation to test descriptor families.
6. Domain sanity check against known PQD physics/chemistry.

## Figure types

For publication-style ML figures:

- Dataset map: composition/synthesis/target distribution.
- Model performance: predicted vs measured with uncertainty and grouped validation.
- Feature importance: restrained bar chart with confidence intervals if possible.
- SHAP beeswarm or compact summary.
- SHAP/PDP dependence plot for key descriptors.
- Mechanism-aware schematic linking features to plausible chemistry.

## Style

- White background.
- Arial/Helvetica-like font.
- Thin axes.
- Colorblind-aware palettes.
- Avoid rainbow unless the quantity is naturally sequential and a colorbar is essential.
- Label units directly on axes.
- Keep figure claims conservative.

## Interpretation language

Preferred:

- “The trained model assigns high importance to...”
- “Within this dataset, higher/lower values of X are associated with...”
- “This trend is consistent with..., but requires experimental validation.”

Avoid:

- “SHAP proves...”
- “The model discovers the true mechanism...”
- “This feature determines the property...”
