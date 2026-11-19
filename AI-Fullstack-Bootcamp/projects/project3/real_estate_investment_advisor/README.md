# 🏠 Real Estate Investment Advisor

Predicts whether a property is a **Good Investment** (classification) and its
**estimated price in 5 years** (regression), with a Streamlit dashboard for
data entry, listing exploration, and EDA. Experiments are tracked with MLflow.

## Files
- `preprocessing.py` – cleaning, feature engineering, target creation (shared by training + app)
- `generate_sample_data.py` – creates a synthetic `india_housing_prices.csv` if you don't have the real Kaggle file
- `train_models.py` – trains 5 classifiers + 5 regressors, logs to MLflow, saves the best of each
- `app.py` – the Streamlit app
- `requirements.txt` – dependencies

## Setup
```bash
pip install -r requirements.txt
```

## 1. Get the data
Put the real dataset at `data/india_housing_prices.csv` (columns: State, City,
Locality, Property_Type, BHK, Size_in_SqFt, Price_in_Lakhs, Price_per_SqFt,
Year_Built, Furnished_Status, Floor_No, Total_Floors, Age_of_Property,
Nearby_Schools, Nearby_Hospitals, Public_Transport_Accessibility,
Parking_Space, Security, Amenities, Facing, Owner_Type, Availability_Status,
RERA_Approved, ...).

Don't have it yet? Generate a synthetic one to test the whole pipeline:
```bash
python generate_sample_data.py --rows 20000
```

## 2. Train the models
```bash
python train_models.py --data data/india_housing_prices.csv
```
This trains **LogisticRegression, DecisionTree, RandomForest,
GradientBoosting, XGBoost** for classification and **LinearRegression, Ridge,
RandomForest, GradientBoosting, XGBoost** for regression, logs params/metrics/
models to MLflow (`sqlite:///mlflow.db`), and saves the best model of each
type to `models/` for the app to use.

To inspect the MLflow experiment UI:
```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

## 3. Launch the app
```bash
streamlit run app.py
```

### App tabs
- **Predict** – fill in property details → get a Good/Not-Good verdict with a
  confidence score, the 5-year price forecast, and feature importance.
- **Explore Listings** – filter the training data by city, price, BHK, etc.
- **Insights** – price-per-sqft by city, price distribution, size vs price,
  good-investment share by city, and a correlation heatmap.

## How the targets are defined
- **Future_Price_5Y** (regression): `Price_in_Lakhs * (1.08)^5` — a fixed 8%
  annual appreciation assumption (adjust `GROWTH_RATE`/`GROWTH_YEARS` in
  `preprocessing.py` to change it, or swap in a location-based rate).
- **Good_Investment** (classification): a multi-factor score — price per sqft
  below the citywide median, BHK ≥ 3, RERA-approved, and ready-to-move each
  contribute a point; a score ≥ 2 is labeled "good investment". Adjust the
  rule in `preprocessing.py::engineer_features`.
