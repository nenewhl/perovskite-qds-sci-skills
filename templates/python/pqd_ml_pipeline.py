#!/usr/bin/env python3
"""
PQD Materials ML Pipeline
-------------------------

A clean, reproducible template for perovskite quantum-dot machine-learning datasets.

Usage:
    python pqd_ml_pipeline.py --data pqd_ml_example.csv --target PLQY --output outputs/pqd_ml_demo

The example data are synthetic. Replace them with real experimental or literature-curated data
before making scientific claims.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor, DummyClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    balanced_accuracy_score,
    f1_score,
    accuracy_score,
)
from sklearn.model_selection import KFold, GroupKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PQD materials ML pipeline template.")
    parser.add_argument("--data", required=True, help="Path to CSV data table.")
    parser.add_argument("--target", required=True, help="Target column name.")
    parser.add_argument("--output", default="outputs/pqd_ml_output", help="Output directory.")
    parser.add_argument("--task", choices=["regression", "classification", "auto"], default="auto")
    parser.add_argument("--group", default=None, help="Optional group column, e.g. source_id or batch_id.")
    parser.add_argument("--exclude", nargs="*", default=[], help="Columns to exclude from features.")
    parser.add_argument("--n-splits", type=int, default=5)
    parser.add_argument("--random-seed", type=int, default=42)
    return parser.parse_args()


def infer_task(y: pd.Series, requested: str) -> str:
    if requested != "auto":
        return requested
    if pd.api.types.is_numeric_dtype(y) and y.nunique(dropna=True) > 10:
        return "regression"
    return "classification"


def split_columns(df: pd.DataFrame, target: str, exclude: List[str]) -> Tuple[List[str], List[str]]:
    feature_df = df.drop(columns=[target] + [c for c in exclude if c in df.columns])
    numeric_cols = feature_df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = [c for c in feature_df.columns if c not in numeric_cols]
    return numeric_cols, categorical_cols


def make_preprocessor(numeric_cols: List[str], categorical_cols: List[str]) -> ColumnTransformer:
    numeric_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, numeric_cols),
            ("cat", categorical_pipe, categorical_cols),
        ],
        remainder="drop",
    )


def build_models(task: str, random_seed: int):
    if task == "regression":
        return {
            "dummy_median": DummyRegressor(strategy="median"),
            "ridge": Ridge(alpha=1.0, random_state=random_seed),
            "random_forest": RandomForestRegressor(
                n_estimators=300,
                max_depth=None,
                min_samples_leaf=2,
                random_state=random_seed,
                n_jobs=-1,
            ),
        }
    return {
        "dummy_most_frequent": DummyClassifier(strategy="most_frequent"),
        "logistic_regression": LogisticRegression(max_iter=500, class_weight="balanced"),
        "random_forest": RandomForestClassifier(
            n_estimators=300,
            min_samples_leaf=2,
            class_weight="balanced",
            random_state=random_seed,
            n_jobs=-1,
        ),
    }


def get_cv(df: pd.DataFrame, group_col: str | None, n_splits: int, random_seed: int):
    if group_col and group_col in df.columns:
        n_groups = df[group_col].nunique()
        actual_splits = min(n_splits, n_groups)
        if actual_splits < 2:
            raise ValueError(f"Not enough groups in {group_col} for GroupKFold.")
        return GroupKFold(n_splits=actual_splits), df[group_col]
    return KFold(n_splits=n_splits, shuffle=True, random_state=random_seed), None


def evaluate_regression(y_true, y_pred):
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": mean_squared_error(y_true, y_pred, squared=False),
        "R2": r2_score(y_true, y_pred),
    }


def run_pipeline(args: argparse.Namespace) -> None:
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.data)
    if args.target not in df.columns:
        raise ValueError(f"Target column '{args.target}' not found. Available columns: {list(df.columns)}")

    df = df.dropna(subset=[args.target]).copy()
    task = infer_task(df[args.target], args.task)

    exclude = list(args.exclude)
    if args.group and args.group not in exclude:
        exclude.append(args.group)

    numeric_cols, categorical_cols = split_columns(df, args.target, exclude)
    feature_cols = numeric_cols + categorical_cols

    X = df[feature_cols]
    y = df[args.target]

    preprocessor = make_preprocessor(numeric_cols, categorical_cols)
    models = build_models(task, args.random_seed)
    cv, groups = get_cv(df, args.group, args.n_splits, args.random_seed)

    if task == "regression":
        scoring = {
            "MAE": "neg_mean_absolute_error",
            "RMSE": "neg_root_mean_squared_error",
            "R2": "r2",
        }
    else:
        scoring = {
            "accuracy": "accuracy",
            "balanced_accuracy": "balanced_accuracy",
            "f1_macro": "f1_macro",
        }

    rows = []
    for model_name, model in models.items():
        pipe = Pipeline(
            steps=[
                ("preprocess", preprocessor),
                ("model", model),
            ]
        )

        scores = cross_validate(
            pipe,
            X,
            y,
            groups=groups,
            cv=cv,
            scoring=scoring,
            return_train_score=False,
            error_score="raise",
        )

        result = {"model": model_name}
        for metric, values in scores.items():
            if not metric.startswith("test_"):
                continue
            clean_metric = metric.replace("test_", "")
            vals = values.copy()
            if clean_metric in ["MAE", "RMSE"]:
                vals = -vals
            result[f"{clean_metric}_mean"] = float(np.mean(vals))
            result[f"{clean_metric}_std"] = float(np.std(vals))
        rows.append(result)

    summary = pd.DataFrame(rows)
    summary.to_csv(out_dir / "model_cv_summary.csv", index=False)

    audit = {
        "data_path": args.data,
        "n_rows_after_target_dropna": int(len(df)),
        "n_features": int(len(feature_cols)),
        "numeric_features": numeric_cols,
        "categorical_features": categorical_cols,
        "target": args.target,
        "task": task,
        "group_column": args.group,
        "excluded_columns": exclude,
        "n_splits": args.n_splits,
        "random_seed": args.random_seed,
    }

    (out_dir / "dataset_audit.json").write_text(
        json_dumps_pretty(audit),
        encoding="utf-8",
    )

    print("Saved:")
    print(f"  {out_dir / 'model_cv_summary.csv'}")
    print(f"  {out_dir / 'dataset_audit.json'}")
    print("\nModel summary:")
    print(summary.to_string(index=False))


def json_dumps_pretty(obj) -> str:
    import json

    return json.dumps(obj, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    run_pipeline(parse_args())
