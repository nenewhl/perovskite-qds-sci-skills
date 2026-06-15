"""Minimal publication-style plot template for spectral or device curves.

Usage:
    python pqd_publication_plot.py input.csv output.pdf

Expected CSV columns:
    x,y
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python pqd_publication_plot.py input.csv output.pdf")

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    df = pd.read_csv(input_path)
    required = {"x", "y"}
    if not required.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {sorted(required)}")

    fig, ax = plt.subplots(figsize=(3.35, 2.45))
    ax.plot(df["x"], df["y"], linewidth=1.2)
    ax.set_xlabel("X")
    ax.set_ylabel("Intensity / a.u.")
    ax.tick_params(direction="out", width=0.8, length=3)
    for spine in ax.spines.values():
        spine.set_linewidth(0.8)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")


if __name__ == "__main__":
    main()
