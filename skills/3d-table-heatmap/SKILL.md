---
name: 3d-table-heatmap
description: Publication-style Python skill for creating pseudo-3D table heatmaps and time-series heatmap blocks. Use when the user asks for 3D表格型热图, 时序热图, 3D柱状热图, LST heatmap, spatiotemporal heatmap, 多区域随时间变化趋势图, or wants to convert Excel/CSV matrix data into a polished scientific heatmap with height-color dual encoding.
---

# 3D Table Heatmap Skill

Use this skill to turn matrix-like scientific data into a high-visual-quality pseudo-3D table heatmap. The output is suitable for academic reports, thesis figures, graphical method demonstrations, and exploratory visualization.

## When to use

Use this skill when the task involves:

- Time-series heatmaps with categories on the y-axis and years/time points on the x-axis.
- Matrix data where value should be encoded by both color and apparent column height.
- Land-surface temperature, PL/RL intensity, PLQY retention, stability, dose-response, aging, batch screening, or multi-sample trend visualization.
- Requests in Chinese such as `高颜值3D表格型时序热图`, `3D柱状热图`, `多配色热图`, `Excel数据绘制热图`.

## Input contract

Preferred table format:

```text
Region,2004,2005,2006,...,2023
Land,16.2,17.1,18.0,...,20.3
Water,9.8,10.5,11.2,...,13.0
Forest,14.5,15.0,15.8,...,18.4
```

The first column is used as the y-axis category index. Remaining columns are x-axis time points. Numeric cells are mapped to both height and color. Missing values should be `NaN`, blank cells, or values that are explicitly defined as missing by the user.

## Workflow

1. Inspect the data shape and confirm the first column should be the y-axis category.
2. Convert the table to a numeric matrix with `df.set_index(first_column)`.
3. Choose a colormap according to use case:
   - `viridis`: safest for publication and colorblind-aware display.
   - `Spectral_r`: good for cold-to-hot scientific gradients.
   - `coolwarm`: intuitive low-high contrast.
   - `turbo`: strong visual impact for reports and social-media tutorials.
4. Set `vmin` and `vmax` explicitly. Do not let extreme outliers silently determine the color scale.
5. Export at 300 dpi for slides or 600 dpi for publication-like raster output. Use PDF/SVG for editable vector output when downstream editing is required.

## Default visual standards

- White or light-gray table background.
- Thin white grid lines.
- No heavy 3D axis box.
- Height-color dual encoding, with a colorbar carrying the exact metric name.
- Avoid decorative gradients unrelated to data.
- Keep missing cells blank; do not interpolate unless the user explicitly asks.

## Recommended outputs

For a substantial request, provide:

1. A cleaned plotting script.
2. A small example CSV/XLSX-compatible data table.
3. At least one exported figure.
4. Brief notes on how to replace the example data with the user's own data.

## Reference files

- `references/data-format.md`: input data conventions and examples.
- `references/plotting-guide.md`: style, colormap, and export guidance.
- `templates/python/advanced_3d_table_heatmap.py`: executable Python template.
- `templates/data/3d_heatmap_example.csv`: minimal example data.
