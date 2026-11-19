"""
train_models.py
----------------
Trains >=5 classification models (target: Good_Investment) and >=5 regression
models (target: Future_Price_5Y), evaluates them, logs everything to MLflow,
and saves the best model of each kind (+ the fitted encoders/scaler) to
disk with joblib so the Streamlit app can load them without needing a
running MLflow server.

Usage:
    python train_models.py --data data/india_housing_prices.csv
"""
import argparse
import os

import joblib
import mlflow
import mlflow.sklearn
import mlflow.xgboost
import numpy as np
import pandas as pd
from sklearn.ensemble import (GradientBoostingClassifier, GradientBoostingRegressor,
                               RandomForestClassifier, RandomForestRegressor)
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge
from sklearn.metrics import (accuracy_score, f1_score, mean_absolute_error,
                              mean_squared_error, precision_score, r2_score,
                              recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier, XGBRegressor

from preprocessing import (CLASSIFICATION_TARGET, REGRESSION_TARGET,
                            build_feature_matrix, full_pipeline)


def log_model_safely(model, name):
    """XGBoost models need the xgboost flavor; everything else uses sklearn."""
    if "XGB" in type(model).__name__:
        mlflow.xgboost.log_model(model, artifact_path="model")
    else:
        mlflow.sklearn.log_model(model, artifact_path="model")


MODEL_DIR = "models"
EXPERIMENT_NAME = "real_estate_investment_advisor"
MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"  # local, zero-setup tracking backend


def get_classifiers():
    return {
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "DecisionTree": DecisionTreeClassifier(max_depth=8, random_state=42),
        "RandomForest": RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42),
        "GradientBoosting": GradientBoostingClassifier(random_state=42),
        "XGBoost": XGBClassifier(random_state=42, eval_metric="logloss"),
    }


def get_regressors():
    return {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "RandomForest": RandomForestRegressor(n_estimators=200, max_depth=12, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(random_state=42),
        "XGBoost": XGBRegressor(random_state=42),
    }


def eval_classifier(model, X_test, y_test):
    preds = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else preds
    return {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, zero_division=0),
        "recall": recall_score(y_test, preds, zero_division=0),
        "f1": f1_score(y_test, preds, zero_division=0),
        "roc_auc": roc_auc_score(y_test, proba),
    }


def eval_regressor(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "rmse": float(np.sqrt(mean_squared_error(y_test, preds))),
        "mae": mean_absolute_error(y_test, preds),
        "r2": r2_score(y_test, preds),
    }


def run(data_path: str):
    os.makedirs(MODEL_DIR, exist_ok=True)
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)

    print(f"Loading + cleaning data from {data_path} ...")
    df = full_pipeline(data_path)
    X, feature_cols, encoders = build_feature_matrix(df, fit=True)

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=feature_cols)

    # ---------------- Classification ----------------
    y_clf = df[CLASSIFICATION_TARGET]
    Xc_train, Xc_test, yc_train, yc_test = train_test_split(
        X_scaled, y_clf, test_size=0.2, random_state=42, stratify=y_clf
    )

    print("\n=== Training classification models (Good_Investment) ===")
    best_clf_name, best_clf, best_clf_score = None, None, -np.inf
    clf_results = {}
    for name, model in get_classifiers().items():
        with mlflow.start_run(run_name=f"clf_{name}"):
            model.fit(Xc_train, yc_train)
            metrics = eval_classifier(model, Xc_test, yc_test)
            mlflow.log_params(model.get_params())
            mlflow.log_metrics(metrics)
            log_model_safely(model, name)
            clf_results[name] = metrics
            print(f"  {name:18s} | acc={metrics['accuracy']:.3f}  f1={metrics['f1']:.3f}  roc_auc={metrics['roc_auc']:.3f}")
            if metrics["f1"] > best_clf_score:
                best_clf_score, best_clf_name, best_clf = metrics["f1"], name, model

    print(f"Best classifier: {best_clf_name} (F1={best_clf_score:.3f})")

    # ---------------- Regression ----------------
    y_reg = df[REGRESSION_TARGET]
    Xr_train, Xr_test, yr_train, yr_test = train_test_split(
        X_scaled, y_reg, test_size=0.2, random_state=42
    )

    print("\n=== Training regression models (Future_Price_5Y) ===")
    best_reg_name, best_reg, best_reg_score = None, None, np.inf
    reg_results = {}
    for name, model in get_regressors().items():
        with mlflow.start_run(run_name=f"reg_{name}"):
            model.fit(Xr_train, yr_train)
            metrics = eval_regressor(model, Xr_test, yr_test)
            mlflow.log_params(model.get_params())
            mlflow.log_metrics(metrics)
            log_model_safely(model, name)
            reg_results[name] = metrics
            print(f"  {name:18s} | rmse={metrics['rmse']:.2f}  mae={metrics['mae']:.2f}  r2={metrics['r2']:.3f}")
            if metrics["rmse"] < best_reg_score:
                best_reg_score, best_reg_name, best_reg = metrics["rmse"], name, model

    print(f"Best regressor: {best_reg_name} (RMSE={best_reg_score:.2f})")

    # ---------------- Persist best models + preprocessing artifacts ----------------
    joblib.dump(best_clf, os.path.join(MODEL_DIR, "best_classifier.pkl"))
    joblib.dump(best_reg, os.path.join(MODEL_DIR, "best_regressor.pkl"))
    joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.pkl"))
    joblib.dump(encoders, os.path.join(MODEL_DIR, "encoders.pkl"))
    joblib.dump(feature_cols, os.path.join(MODEL_DIR, "feature_cols.pkl"))
    joblib.dump({"classifier": best_clf_name, "regressor": best_reg_name},
                os.path.join(MODEL_DIR, "best_model_names.pkl"))
    joblib.dump(clf_results, os.path.join(MODEL_DIR, "clf_results.pkl"))
    joblib.dump(reg_results, os.path.join(MODEL_DIR, "reg_results.pkl"))

    # feature importance for the app (if the winning model supports it)
    importance = None
    if hasattr(best_clf, "feature_importances_"):
        importance = dict(zip(feature_cols, best_clf.feature_importances_))
    joblib.dump(importance, os.path.join(MODEL_DIR, "clf_feature_importance.pkl"))

    importance_r = None
    if hasattr(best_reg, "feature_importances_"):
        importance_r = dict(zip(feature_cols, best_reg.feature_importances_))
    joblib.dump(importance_r, os.path.join(MODEL_DIR, "reg_feature_importance.pkl"))

    # save a small cleaned sample of the data for the app's EDA tab
    df.to_csv(os.path.join(MODEL_DIR, "processed_data_sample.csv"), index=False)

    print(f"\nSaved best models + artifacts to '{MODEL_DIR}/'.")
    print("Launch the app with:  streamlit run app.py")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="data/india_housing_prices.csv")
    args = parser.parse_args()
    run(args.data)
