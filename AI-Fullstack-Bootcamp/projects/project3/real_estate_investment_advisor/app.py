"""
app.py
------
Streamlit UI for the Real Estate Investment Advisor.

Tabs:
  1. Predict        - form to enter property details -> Good Investment? + 5Y price forecast
  2. Explore Data    - filter existing listings by area/price/BHK etc.
  3. Insights (EDA)  - location-wise trends, correlations, charts

Run:
    streamlit run app.py
"""
import os

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from preprocessing import (CATEGORICAL_FEATURES, CLASSIFICATION_TARGET,
                            NUMERIC_FEATURES, REGRESSION_TARGET,
                            build_feature_matrix)

MODEL_DIR = "models"

st.set_page_config(page_title="Real Estate Investment Advisor", layout="wide", page_icon="🏠")


# ----------------------------------------------------------------------------
# Cached loaders
# ----------------------------------------------------------------------------
@st.cache_resource
def load_artifacts():
    required = ["best_classifier.pkl", "best_regressor.pkl", "scaler.pkl",
                "encoders.pkl", "feature_cols.pkl", "best_model_names.pkl"]
    missing = [f for f in required if not os.path.exists(os.path.join(MODEL_DIR, f))]
    if missing:
        return None

    artifacts = {
        "clf": joblib.load(os.path.join(MODEL_DIR, "best_classifier.pkl")),
        "reg": joblib.load(os.path.join(MODEL_DIR, "best_regressor.pkl")),
        "scaler": joblib.load(os.path.join(MODEL_DIR, "scaler.pkl")),
        "encoders": joblib.load(os.path.join(MODEL_DIR, "encoders.pkl")),
        "feature_cols": joblib.load(os.path.join(MODEL_DIR, "feature_cols.pkl")),
        "model_names": joblib.load(os.path.join(MODEL_DIR, "best_model_names.pkl")),
    }
    for optional in ["clf_results.pkl", "reg_results.pkl",
                      "clf_feature_importance.pkl", "reg_feature_importance.pkl"]:
        p = os.path.join(MODEL_DIR, optional)
        artifacts[optional.replace(".pkl", "")] = joblib.load(p) if os.path.exists(p) else None
    return artifacts


@st.cache_data
def load_sample_data():
    p = os.path.join(MODEL_DIR, "processed_data_sample.csv")
    if os.path.exists(p):
        return pd.read_csv(p)
    return None


def option_list(encoders, col, fallback):
    if encoders and col in encoders:
        return list(encoders[col].classes_)
    return fallback


# ----------------------------------------------------------------------------
# App
# ----------------------------------------------------------------------------
st.title("🏠 Real Estate Investment Advisor")
st.caption("Predicting property profitability & 5-year future value")

artifacts = load_artifacts()
sample_df = load_sample_data()

if artifacts is None:
    st.warning(
        "No trained models found yet. Run the training pipeline first:\n\n"
        "```bash\npython generate_sample_data.py   # only if you don't have the real dataset\n"
        "python train_models.py --data data/india_housing_prices.csv\n```\n"
        "Then relaunch this app."
    )
    st.stop()

tab_predict, tab_explore, tab_insights = st.tabs(["🔮 Predict", "🔍 Explore Listings", "📊 Insights"])

# =============================================================================
# TAB 1 — PREDICT
# =============================================================================
with tab_predict:
    st.subheader("Enter property details")

    encoders = artifacts["encoders"]
    col1, col2, col3 = st.columns(3)

    with col1:
        state = st.selectbox("State", option_list(encoders, "State", ["Maharashtra", "Karnataka", "Delhi"]))
        city = st.selectbox("City", option_list(encoders, "City", ["Mumbai", "Bengaluru", "New Delhi"]))
        property_type = st.selectbox("Property Type", option_list(encoders, "Property_Type", ["Apartment", "Villa"]))
        bhk = st.slider("BHK", 1, 6, 3)
        size_sqft = st.number_input("Size (Sq Ft)", min_value=200, max_value=10000, value=1200, step=50)

    with col2:
        price_in_lakhs = st.number_input("Current Price (₹ Lakhs)", min_value=1.0, max_value=100000.0, value=80.0, step=1.0)
        year_built = st.number_input("Year Built", min_value=1950, max_value=2024, value=2015, step=1)
        floor_no = st.number_input("Floor No.", min_value=0, max_value=100, value=3, step=1)
        total_floors = st.number_input("Total Floors", min_value=1, max_value=100, value=12, step=1)
        furnished_status = st.selectbox("Furnished Status", option_list(encoders, "Furnished_Status", ["Furnished", "Semi-Furnished", "Unfurnished"]))

    with col3:
        nearby_schools = st.slider("Nearby Schools", 0, 15, 3)
        nearby_hospitals = st.slider("Nearby Hospitals", 0, 15, 2)
        transport = st.selectbox("Public Transport Access", option_list(encoders, "Public_Transport_Accessibility", ["High", "Medium", "Low"]))
        parking = st.selectbox("Parking Space", option_list(encoders, "Parking_Space", ["Yes", "No"]))
        security = st.selectbox("Security", option_list(encoders, "Security", ["Yes", "No"]))

    col4, col5, col6, col7 = st.columns(4)
    with col4:
        facing = st.selectbox("Facing", option_list(encoders, "Facing", ["North", "South", "East", "West"]))
    with col5:
        owner_type = st.selectbox("Owner Type", option_list(encoders, "Owner_Type", ["Owner", "Broker", "Builder"]))
    with col6:
        availability = st.selectbox("Availability", option_list(encoders, "Availability_Status", ["Ready_to_move", "Under_Construction"]))
    with col7:
        rera = st.selectbox("RERA Approved", option_list(encoders, "RERA_Approved", ["Yes", "No"]))

    amenity_count = st.slider("Number of Amenities (gym, pool, garden, etc.)", 0, 10, 3)

    if st.button("🔍 Analyze Investment", type="primary", use_container_width=True):
        price_per_sqft = (price_in_lakhs * 100000) / size_sqft
        age_of_property = 2024 - year_built
        floor_ratio = (floor_no + 1) / max(total_floors, 1)

        raw_row = pd.DataFrame([{
            "State": state, "City": city, "Property_Type": property_type,
            "BHK": bhk, "Size_in_SqFt": size_sqft, "Price_per_SqFt": price_per_sqft,
            "Year_Built": year_built, "Furnished_Status": furnished_status,
            "Floor_No": floor_no, "Total_Floors": total_floors,
            "Age_of_Property": age_of_property, "Nearby_Schools": nearby_schools,
            "Nearby_Hospitals": nearby_hospitals, "Amenity_Count": amenity_count,
            "Floor_Ratio": floor_ratio,
            "Public_Transport_Accessibility": transport, "Parking_Space": parking,
            "Security": security, "Facing": facing, "Owner_Type": owner_type,
            "Availability_Status": availability, "RERA_Approved": rera,
        }])

        X_input, _, _ = build_feature_matrix(raw_row, encoders=encoders, fit=False)
        X_input = X_input[artifacts["feature_cols"]]
        X_scaled = artifacts["scaler"].transform(X_input)

        clf_pred = artifacts["clf"].predict(X_scaled)[0]
        clf_proba = (artifacts["clf"].predict_proba(X_scaled)[0][1]
                     if hasattr(artifacts["clf"], "predict_proba") else None)
        reg_pred = artifacts["reg"].predict(X_scaled)[0]

        st.markdown("---")
        r1, r2 = st.columns(2)
        with r1:
            if clf_pred == 1:
                st.success("✅ **Good Investment**")
            else:
                st.error("❌ **Not a Recommended Investment**")
            if clf_proba is not None:
                st.metric("Model Confidence", f"{clf_proba*100:.1f}%")
                st.progress(min(max(clf_proba, 0.0), 1.0))
        with r2:
            st.metric("Estimated Price in 5 Years", f"₹ {reg_pred:,.1f} Lakhs",
                       delta=f"+{reg_pred - price_in_lakhs:,.1f} Lakhs ({(reg_pred/price_in_lakhs - 1)*100:.1f}%)")

        st.caption(f"Models used — Classification: **{artifacts['model_names']['classifier']}**, "
                   f"Regression: **{artifacts['model_names']['regressor']}**")

        fi = artifacts.get("clf_feature_importance")
        if fi:
            st.markdown("#### Feature Importance (Investment Classification)")
            fi_df = pd.DataFrame(sorted(fi.items(), key=lambda x: -x[1])[:10],
                                  columns=["Feature", "Importance"])
            fig = px.bar(fi_df, x="Importance", y="Feature", orientation="h")
            fig.update_layout(yaxis={"categoryorder": "total ascending"}, height=350)
            st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# TAB 2 — EXPLORE LISTINGS
# =============================================================================
with tab_explore:
    st.subheader("Filter properties")
    if sample_df is None:
        st.info("No processed dataset found. Train the models first to populate this view.")
    else:
        f1, f2, f3, f4 = st.columns(4)
        with f1:
            cities = st.multiselect("City", sorted(sample_df["City"].unique()))
        with f2:
            price_range = st.slider(
                "Price (₹ Lakhs)",
                float(sample_df["Price_in_Lakhs"].min()), float(sample_df["Price_in_Lakhs"].max()),
                (float(sample_df["Price_in_Lakhs"].min()), float(sample_df["Price_in_Lakhs"].max())),
            )
        with f3:
            bhk_filter = st.multiselect("BHK", sorted(sample_df["BHK"].unique()))
        with f4:
            good_only = st.checkbox("Good Investments only")

        filtered = sample_df.copy()
        if cities:
            filtered = filtered[filtered["City"].isin(cities)]
        if bhk_filter:
            filtered = filtered[filtered["BHK"].isin(bhk_filter)]
        filtered = filtered[filtered["Price_in_Lakhs"].between(*price_range)]
        if good_only:
            filtered = filtered[filtered[CLASSIFICATION_TARGET] == 1]

        st.write(f"**{len(filtered):,} properties match your filters**")
        display_cols = ["City", "Locality", "Property_Type", "BHK", "Size_in_SqFt",
                         "Price_in_Lakhs", "Price_per_SqFt", CLASSIFICATION_TARGET, REGRESSION_TARGET]
        display_cols = [c for c in display_cols if c in filtered.columns]
        st.dataframe(filtered[display_cols].head(500), use_container_width=True)

# =============================================================================
# TAB 3 — INSIGHTS / EDA
# =============================================================================
with tab_insights:
    st.subheader("Market insights")
    if sample_df is None:
        st.info("No processed dataset found. Train the models first to populate this view.")
    else:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Average price per sq ft by city**")
            avg_price = sample_df.groupby("City")["Price_per_SqFt"].mean().sort_values(ascending=False).reset_index()
            fig = px.bar(avg_price, x="City", y="Price_per_SqFt")
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.markdown("**Price distribution**")
            fig = px.histogram(sample_df, x="Price_in_Lakhs", nbins=40)
            st.plotly_chart(fig, use_container_width=True)

        c3, c4 = st.columns(2)
        with c3:
            st.markdown("**Size vs Price**")
            plot_df = sample_df.sample(min(2000, len(sample_df)), random_state=1)
            fig = px.scatter(plot_df, x="Size_in_SqFt", y="Price_in_Lakhs", color="City", opacity=0.6)
            st.plotly_chart(fig, use_container_width=True)

        with c4:
            st.markdown("**Good Investment share by city**")
            share = sample_df.groupby("City")[CLASSIFICATION_TARGET].mean().sort_values(ascending=False).reset_index()
            share[CLASSIFICATION_TARGET] = share[CLASSIFICATION_TARGET] * 100
            fig = px.bar(share, x="City", y=CLASSIFICATION_TARGET, labels={CLASSIFICATION_TARGET: "% Good Investment"})
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Correlation heatmap (numeric features)**")
        num_cols = [c for c in NUMERIC_FEATURES + [REGRESSION_TARGET] if c in sample_df.columns]
        corr = sample_df[num_cols].corr()
        fig = px.imshow(corr, text_auto=".2f", aspect="auto", color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
        st.plotly_chart(fig, use_container_width=True)

        # Model performance comparison
        if artifacts.get("clf_results") or artifacts.get("reg_results"):
            st.markdown("---")
            st.markdown("### Model comparison (from training run)")
            m1, m2 = st.columns(2)
            if artifacts.get("clf_results"):
                with m1:
                    st.markdown("**Classification models**")
                    st.dataframe(pd.DataFrame(artifacts["clf_results"]).T.style.format("{:.3f}"),
                                 use_container_width=True)
            if artifacts.get("reg_results"):
                with m2:
                    st.markdown("**Regression models**")
                    st.dataframe(pd.DataFrame(artifacts["reg_results"]).T.style.format("{:.3f}"),
                                 use_container_width=True)

st.markdown("---")
st.caption("Built with Streamlit · scikit-learn · XGBoost · MLflow")
