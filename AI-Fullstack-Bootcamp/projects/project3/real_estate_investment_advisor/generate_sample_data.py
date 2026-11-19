"""
generate_sample_data.py
------------------------
Creates a synthetic 'india_housing_prices.csv' that mirrors the schema of the
Kaggle "India Housing Prices Dataset" referenced in the project brief.

Only needed if you don't already have the real dataset. If you have the real
india_housing_prices.csv, just drop it in the `data/` folder and skip this
script entirely -- every other script will pick it up automatically.

Usage:
    python generate_sample_data.py --rows 20000
"""
import argparse
import os
import numpy as np
import pandas as pd

STATES_CITIES = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Karnataka": ["Bengaluru", "Mysuru"],
    "Delhi": ["New Delhi"],
    "Telangana": ["Hyderabad", "Warangal"],
    "Tamil Nadu": ["Chennai", "Coimbatore"],
    "West Bengal": ["Kolkata", "Howrah"],
    "Gujarat": ["Ahmedabad", "Surat"],
    "Uttar Pradesh": ["Lucknow", "Noida"],
    "Rajasthan": ["Jaipur", "Udaipur"],
    "Punjab": ["Chandigarh", "Ludhiana"],
}

PROPERTY_TYPES = ["Apartment", "Villa", "Independent House", "Studio", "Penthouse"]
FURNISHED_STATUS = ["Furnished", "Semi-Furnished", "Unfurnished"]
FACING = ["North", "South", "East", "West", "North-East", "South-West"]
OWNER_TYPE = ["Owner", "Broker", "Builder"]
AVAILABILITY = ["Ready_to_move", "Under_Construction"]
PARKING = ["Yes", "No"]
AMENITY_POOL = ["gym", "pool", "garden", "clubhouse", "playground", "security",
                "power_backup", "lift", "sports_court", "spa"]


def make_amenities(rng):
    n = rng.integers(0, 6)
    return ", ".join(rng.choice(AMENITY_POOL, size=n, replace=False)) if n else "none"


def generate(rows: int, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    states = list(STATES_CITIES.keys())

    records = []
    for i in range(rows):
        state = rng.choice(states)
        city = rng.choice(STATES_CITIES[state])
        property_type = rng.choice(PROPERTY_TYPES)
        bhk = int(rng.integers(1, 6))
        size_sqft = int(rng.normal(600 * bhk, 250))
        size_sqft = max(250, size_sqft)

        # base price per sqft varies by state/city tier + noise
        tier_multiplier = {"Mumbai": 3.2, "New Delhi": 2.6, "Bengaluru": 2.4,
                            "Chennai": 1.9, "Hyderabad": 1.8, "Pune": 1.7,
                            "Kolkata": 1.6, "Ahmedabad": 1.4}.get(city, 1.0)
        price_per_sqft = max(800, rng.normal(3500 * tier_multiplier, 700))

        price_in_lakhs = round((price_per_sqft * size_sqft) / 100000, 2)

        year_built = int(rng.integers(1980, 2024))
        age_of_property = 2024 - year_built
        floor_no = int(rng.integers(0, 25))
        total_floors = int(floor_no + rng.integers(1, 15))

        record = {
            "Property_ID": f"P{i+1:06d}",
            "State": state,
            "City": city,
            "Locality": f"{city}_Sector_{int(rng.integers(1, 40))}",
            "Property_Type": property_type,
            "BHK": bhk,
            "Size_in_SqFt": size_sqft,
            "Price_in_Lakhs": price_in_lakhs,
            "Price_per_SqFt": round(price_per_sqft, 2),
            "Year_Built": year_built,
            "Furnished_Status": rng.choice(FURNISHED_STATUS),
            "Floor_No": floor_no,
            "Total_Floors": total_floors,
            "Age_of_Property": age_of_property,
            "Nearby_Schools": int(rng.integers(0, 10)),
            "Nearby_Hospitals": int(rng.integers(0, 8)),
            "Public_Transport_Accessibility": rng.choice(["High", "Medium", "Low"]),
            "Parking_Space": rng.choice(PARKING),
            "Security": rng.choice(["Yes", "No"]),
            "Amenities": make_amenities(rng),
            "Facing": rng.choice(FACING),
            "Owner_Type": rng.choice(OWNER_TYPE),
            "Availability_Status": rng.choice(AVAILABILITY),
            "RERA_Approved": rng.choice(["Yes", "No"]),
        }
        records.append(record)

    df = pd.DataFrame(records)

    # inject a few missing values & duplicates so preprocessing has real work to do
    for col in ["Nearby_Schools", "Nearby_Hospitals", "Public_Transport_Accessibility", "Price_per_SqFt"]:
        mask = rng.random(len(df)) < 0.02
        df.loc[mask, col] = np.nan
    df = pd.concat([df, df.sample(frac=0.01, random_state=seed)], ignore_index=True)

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=20000)
    parser.add_argument("--out", type=str, default="data/india_housing_prices.csv")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    df = generate(args.rows)
    df.to_csv(args.out, index=False)
    print(f"Wrote {len(df):,} rows to {args.out}")
