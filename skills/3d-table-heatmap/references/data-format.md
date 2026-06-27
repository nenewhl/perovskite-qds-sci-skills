# Data format for 3D table heatmaps

## Required wide-table structure

Use a wide matrix where rows are categories/samples and columns are time points or conditions.

```csv
Region,2004,2005,2006,2007
Land,16.2,17.1,18.0,18.6
Water,9.8,10.5,11.2,11.4
Forest,14.5,15.0,15.8,16.1
Urban,22.1,22.8,23.4,24.0
```

The first column can be named `Region`, `Sample`, `Composition`, `Condition`, or another category label. In code, use:

```python
df_real = pd.read_excel("data.xlsx")
df_plot = df_real.set_index("Region")
```

For CSV:

```python
df_real = pd.read_csv("data.csv")
df_plot = df_real.set_index("Region")
```

## Missing values

Use blank cells or `NaN` for missing measurements. The plotting template leaves these cells empty. This is preferred for real scientific data because it avoids implying fabricated continuity.

Values `<= 0` are treated as empty by the default template because many heatmap examples use zero as a missing-value placeholder. If zero is a meaningful value in the user's dataset, change this condition:

```python
if np.isnan(val) or val <= 0:
    continue
```

to:

```python
if np.isnan(val):
    continue
```

## Scientific examples

The same layout can represent:

- `Region × Year`: land-surface temperature or environmental index.
- `Sample × Aging time`: PL intensity retention, PLQY retention, RL stability.
- `Composition × Dose`: X-ray response intensity, sensitivity, or damage factor.
- `Film thickness × Time`: scintillator film optimization trends.
- `Batch × Storage days`: reproducibility and stability screening.

## Quality checks before plotting

- Confirm all plotted cells are numeric.
- Confirm the category order is intentional.
- Confirm units are defined in the colorbar label.
- Use fixed `vmin` and `vmax` when comparing several heatmaps.
