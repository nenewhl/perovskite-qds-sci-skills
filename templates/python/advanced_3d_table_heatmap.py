import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon, Rectangle
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def _adjust_color(color, factor=0.85):
    """factor < 1 darkens color; factor > 1 lightens color."""
    rgb = np.array(mpl.colors.to_rgb(color))
    if factor < 1:
        return tuple(rgb * factor)
    return tuple(1 - (1 - rgb) / factor)


def plot_3d_table_heatmap(
    df,
    cmap_name="turbo",
    vmin=0,
    vmax=30,
    title="Spatiotemporal LST variation by region type",
    value_label="LST",
    output_path="advanced_3d_table_heatmap.png",
    dpi=300
):
    """
    df: rows = regions/types, columns = years/time points, values = LST or other metrics.
        NaN or values <= 0 are treated as missing and are not drawn.
    """
    values = df.values.astype(float)
    n_rows, n_cols = values.shape

    cmap = plt.get_cmap(cmap_name)
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

    fig, ax = plt.subplots(figsize=(12.2, 6.6))
    ax.set_facecolor("#eeeeee")

    ax.add_patch(Rectangle((0, 0), n_cols, n_rows, facecolor="#eeeeee", edgecolor="none", zorder=0))
    for x in range(n_cols + 1):
        ax.axvline(x, color="white", lw=1.25, zorder=1)
    for y in range(n_rows + 1):
        ax.axhline(y, color="white", lw=1.25, zorder=1)

    bar_w = 0.62
    bar_d = 0.52
    pad_x = (1 - bar_w) / 2
    pad_y = (1 - bar_d) / 2
    max_lift = 0.76
    min_lift = 0.08
    x_slant = 0.18

    cells = [(i, j) for j in range(n_rows) for i in range(n_cols)]
    cells = sorted(cells, key=lambda t: (-t[1], t[0]))

    for i, j in cells:
        val = values[j, i]
        if np.isnan(val) or val <= 0:
            continue

        frac = np.clip((val - vmin) / (vmax - vmin), 0, 1)
        lift_y = min_lift + frac * max_lift
        lift_x = x_slant * (0.35 + frac)

        x0 = i + pad_x
        y0 = j + pad_y
        w = bar_w
        d = bar_d

        A = np.array([x0, y0])
        B = np.array([x0 + w, y0])
        C = np.array([x0 + w, y0 + d])
        D = np.array([x0, y0 + d])
        V = np.array([lift_x, lift_y])

        A2, B2, C2, D2 = A + V, B + V, C + V, D + V

        base_color = cmap(norm(val))
        front_color = _adjust_color(base_color, 0.72)
        right_color = _adjust_color(base_color, 0.82)
        top_color = _adjust_color(base_color, 1.08)

        shadow = Polygon([A + [0.05, -0.04], B + [0.05, -0.04], C + [0.05, -0.04], D + [0.05, -0.04]],
                         closed=True, facecolor=(0, 0, 0, 0.08), edgecolor="none", zorder=2)
        ax.add_patch(shadow)

        front = Polygon([A, B, B2, A2], closed=True, facecolor=front_color,
                        edgecolor=(1, 1, 1, 0.56), lw=0.45, zorder=3 + j * 0.01)
        right = Polygon([B, C, C2, B2], closed=True, facecolor=right_color,
                        edgecolor=(1, 1, 1, 0.50), lw=0.45, zorder=4 + j * 0.01)
        top = Polygon([A2, B2, C2, D2], closed=True, facecolor=top_color,
                      edgecolor=(1, 1, 1, 0.72), lw=0.55, zorder=5 + j * 0.01)

        ax.add_patch(front)
        ax.add_patch(right)
        ax.add_patch(top)

    ax.set_xlim(-0.10, n_cols + 0.55)
    ax.set_ylim(-0.10, n_rows + 0.92)
    ax.set_aspect("equal")

    ax.set_xticks(np.arange(n_cols) + 0.5)
    ax.set_xticklabels(df.columns, rotation=90, fontsize=8.8)
    ax.set_yticks(np.arange(n_rows) + 0.5)
    ax.set_yticklabels(df.index, fontsize=9.5)

    ax.set_xlabel("Time", fontsize=13, labelpad=10, fontweight="bold")
    ax.set_ylabel("Regions", fontsize=13, labelpad=10, fontweight="bold")
    ax.set_title(title, fontsize=15.5, fontweight="bold", pad=16)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(axis="both", length=0)
    ax.grid(False)

    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    cax = inset_axes(
        ax,
        width="2.2%",
        height="58%",
        loc="lower left",
        bbox_to_anchor=(1.025, 0.19, 1, 1),
        bbox_transform=ax.transAxes,
        borderpad=0
    )
    cbar = plt.colorbar(sm, cax=cax)
    cbar.ax.set_title(value_label, fontsize=12.5, fontweight="bold", pad=10, loc="left")
    cbar.ax.tick_params(labelsize=8.5, length=0)
    cbar.outline.set_visible(False)

    fig.subplots_adjust(left=0.09, right=0.88, bottom=0.20, top=0.88)
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    # Excel 格式要求：
    # 第一列：Region
    # 后续列：2004, 2005, ..., 2023 或其他时间点
    #
    # df_real = pd.read_excel("data.xlsx")
    # df_plot = df_real.set_index("Region")

    np.random.seed(42)
    years = list(range(2004, 2024))
    regions = ["Land", "Water", "Forest", "Urban", "Grassland", "Wetland", "Bare land", "Shrub", "Meadow", "Marsh"]

    baseline = np.array([17, 10, 14, 22, 16, 12, 25, 15, 13, 11], dtype=float)
    trend = np.linspace(-1.8, 3.6, len(years))
    seasonal_like = 1.8 * np.sin(np.linspace(0, 3*np.pi, len(years)))

    data = []
    for b in baseline:
        row = b + trend + seasonal_like + np.random.normal(0, 1.2, len(years))
        data.append(row)

    data = np.clip(np.array(data), 0, 30)
    data[1, [0, 5, 9, 14]] = np.nan
    data[5, [3, 8, 17]] = np.nan
    data[9, [1, 2, 12, 19]] = np.nan

    df_plot = pd.DataFrame(data, index=regions, columns=years)
    df_plot.index.name = "Region"

    plot_3d_table_heatmap(
        df_plot,
        cmap_name="turbo",
        vmin=0,
        vmax=30,
        title="Spatiotemporal LST variation by region type",
        value_label="LST",
        output_path="advanced_3d_table_heatmap.png",
        dpi=300
    )
