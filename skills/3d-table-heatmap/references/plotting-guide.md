# Plotting guide for pseudo-3D table heatmaps

## Concept

This chart is a pseudo-3D heatmap, not a true `mpl_toolkits.mplot3d` bar chart. Each cube is built from 2D polygons. This approach gives cleaner figure control, better annotation behavior, easier export, and a more journal-friendly result.

## Encoding

Each cell uses dual encoding:

- Height: proportional to the normalized value.
- Color: mapped with the selected colormap.

This makes high-value cells visually prominent while keeping the table-like layout readable.

## Colormap choices

Recommended options:

- `viridis`: robust, perceptually ordered, best default for scientific figures.
- `Spectral_r`: intuitive blue-to-red cold-hot interpretation.
- `coolwarm`: simple low-to-high diverging display; good when values represent colder/warmer deviation.
- `plasma`: high contrast for presentations.
- `turbo`: visually striking; best for demonstrations and social-media posts, but use carefully for formal papers.

## Export settings

Use:

```python
plot_3d_table_heatmap(df_plot, dpi=300, output_path="figure.png")
```

For journal-like raster output, use `dpi=600`. For editable output, replace the save line with:

```python
fig.savefig("figure.pdf", bbox_inches="tight")
fig.savefig("figure.svg", bbox_inches="tight")
```

## Layout tuning

Key parameters inside the template:

- `bar_w`: cube width along x.
- `bar_d`: cube footprint depth.
- `max_lift`: maximum visual height.
- `x_slant`: pseudo-3D horizontal slant.
- `vmin`, `vmax`: color and height normalization range.

For dense matrices, reduce `bar_w`, reduce label font size, and increase figure width.

## Common fixes

If labels overlap:

```python
ax.set_xticklabels(df.columns, rotation=90, fontsize=8)
```

If the figure is too flat:

```python
max_lift = 0.95
```

If the figure is too crowded:

```python
bar_w = 0.50
bar_d = 0.42
```

If zero is meaningful:

```python
if np.isnan(val):
    continue
```

instead of skipping `val <= 0`.
