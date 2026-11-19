"""
preprocessing.py
-----------------
Shared data-cleaning / feature-engineering logic used by both the training
script (train_models.py) and the Streamlit app (app.py), so predictions are
always built from the exact same pipeline the models were trained on.
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

NUMERIC_FEATURES = [
    "BHK", "Size_in_SqFt", "Price_per_SqFt", "Year_Built", "Floor_No",
    "Total_Floors", "Age_of_Property", "Nearby_Schools", "Nearby_Hospitals",
    "Amenity_Count", "Floor_Ratio",
]

CATEGORICAL_FEATURES = [
    "State", "City", "Property_Type", "Furnished_Status",
    "Public_Transport_Accessibility", "Parking_Space", "Security",
    "Facing", "Owner_Type", "Availability_Status", "RERA_Approved",
]

CLASSIFICATION_TARGET = "Good_Investment"
REGRESSION_TARGET = "Future_Price_5Y"

GROWTH_RATE = 0.08          # fixed annual appreciation assumption
GROWTH_YEARS = 5


def load_raw(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def _amenity_count(value) -> int:
    if pd.isna(value) or str(value).strip().lower() == "none":
        return 0
    return len([a for a in str(value).split(",") if a.strip()])


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values and duplicates."""
    df = df.copy()
    df = df.drop_duplicates()

    # numeric columns -> median impute
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())

    # categorical columns -> mode impute
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].mode(dropna=True)[0])

    return df.reset_index(drop=True)


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create derived features: price per sqft (if missing), amenity density,
    floor ratio, and the two target variables."""
    df = df.copy()

    if "Price_per_SqFt" not in df.columns or df["Price_per_SqFt"].isna().all():
        df["Price_per_SqFt"] = df["Price_in_Lakhs"] * 100000 / df["Size_in_SqFt"]

    if "Age_of_Property" not in df.columns:
        df["Age_of_Property"] = 2024 - df["Year_Built"]

    df["Amenity_Count"] = df["Amenities"].apply(_amenity_count) if "Amenities" in df.columns else 0
    df["Floor_Ratio"] = (df["Floor_No"] + 1) / df["Total_Floors"].replace(0, 1)

    # ---- Regression target: fixed-rate future value ----
    df[REGRESSION_TARGET] = df["Price_in_Lakhs"] * (1 + GROWTH_RATE) ** GROWTH_YEARS

    # ---- Classification target: multi-factor "Good Investment" score ----
    median_price_per_sqft = df["Price_per_SqFt"].median()
    price_ok = (df["Price_per_SqFt"] <= median_price_per_sqft).astype(int)
    bhk_ok = (df["BHK"] >= 3).astype(int)
    rera_ok = (df.get("RERA_Approved", "No") == "Yes").astype(int) if "RERA_Approved" in df.columns else 0
    ready_ok = (df.get("Availability_Status", "") == "Ready_to_move").astype(int) if "Availability_Status" in df.columns else 0

    score = price_ok + bhk_ok + rera_ok + ready_ok
    df[CLASSIFICATION_TARGET] = (score >= 2).astype(int)

    return df


def encode_features(df: pd.DataFrame, encoders: dict | None = None, fit: bool = True):
    """Label-encode categorical columns. Returns (df_encoded, encoders)."""
    df = df.copy()
    encoders = encoders or {}

    for col in CATEGORICAL_FEATURES:
        if col not in df.columns:
            continue
        if fit:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            encoders[col] = le
        else:
            le = encoders[col]
            # map unseen categories to a safe fallback (first known class)
            df[col] = df[col].astype(str).map(
                lambda v: v if v in le.classes_ else le.classes_[0]
            )
            df[col] = le.transform(df[col])

    return df, encoders


def build_feature_matrix(df: pd.DataFrame, encoders: dict | None = None, fit: bool = True):
    df_encoded, encoders = encode_features(df, encoders=encoders, fit=fit)
    feature_cols = [c for c in NUMERIC_FEATURES + CATEGORICAL_FEATURES if c in df_encoded.columns]
    X = df_encoded[feature_cols]
    return X, feature_cols, encoders


def full_pipeline(path: str):
    """Convenience: raw csv -> cleaned, feature-engineered dataframe."""
    df = load_raw(path)
    df = clean_data(df)
    df = engineer_features(df)
    return df
