# Example: 3D table heatmap

This example uses `templates/data/3d_heatmap_example.csv` and `templates/python/advanced_3d_table_heatmap.py`.

## Run

```bash
pip install numpy pandas matplotlib openpyxl
python templates/python/advanced_3d_table_heatmap.py
```

To use your own Excel file:

```python
df_real = pd.read_excel("data.xlsx")
df_plot = df_real.set_index("Region")
plot_3d_table_heatmap(df_plot, cmap_name="viridis", vmin=0, vmax=30)
```

## Suggested scientific adaptations

For perovskite quantum-dot and scintillator work, replace the axes as follows:

- X axis: aging time, irradiation time, X-ray dose, storage day, or film thickness.
- Y axis: FA, FA/SiO2, FA/ZnS, different ligand treatments, or different film formulations.
- Value/colorbar: PL intensity, RL intensity, PLQY, retention, sensitivity, or normalized response.
