#!/usr/bin/env python3
"""
PQD Interpretability Template
-----------------------------

Template for permutation importance and simple publication-style plots.
SHAP can be added when the local environment has `shap` installed.

Usage:
    Adapt this file after training a model pipeline from pqd_ml_pipeline.py.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.inspection import permutation_importance


def plot_permutation_importance(
    model,
    X,
    y,
    feature_names,
    output_path="permutation_importance.png",
    n_repeats=20,
    random_state=42,
    scoring=None,
):
    """Plot compact permutation importance with error bars."""
    result = permutation_importance(
        model,
        X,
        y,
        n_repeats=n_repeats,
        random_state=random_state,
        scoring=scoring,
        n_jobs=-1,
    )

    imp = pd.DataFrame(
        {
            "feature": feature_names,
            "importance_mean": result.importances_mean,
            "importance_std": result.importances_std,
        }
    ).sort_values("importance_mean", ascending=False)

    top = imp.head(15).iloc[::-1]

    fig, ax = plt.subplots(figsize=(5.2, 4.6))
    ax.barh(top["feature"], top["importance_mean"], xerr=top["importance_std"])
    ax.set_xlabel("Permutation importance")
    ax.set_ylabel("")
    ax.set_title("Feature importance", fontweight="bold")
    ax.tick_params(axis="both", labelsize=8)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return imp


def plot_predicted_vs_measured(
    y_true,
    y_pred,
    output_path="predicted_vs_measured.png",
    xlabel="Measured",
    ylabel="Predicted",
):
    """Publication-style measured-vs-predicted scatter plot."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    fig, ax = plt.subplots(figsize=(4.3, 4.1))
    ax.scatter(y_true, y_pred, s=32, alpha=0.82)

    lo = min(np.nanmin(y_true), np.nanmin(y_pred))
    hi = max(np.nanmax(y_true), np.nanmax(y_pred))
    ax.plot([lo, hi], [lo, hi], lw=1.0, linestyle="--")

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title("Model validation", fontweight="bold")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def shap_note():
    return (
        "For SHAP analysis, install shap and use the trained model carefully. "
        "For tree models, shap.TreeExplainer is usually appropriate. "
        "For pipelines with preprocessing, export transformed feature names before plotting. "
        "Do not interpret SHAP importance as direct proof of physical mechanism."
    )
