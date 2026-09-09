# 1. Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings as wr

wr.filterwarnings("ignore")

# 2. Reading Dataset 
data = pd.read_csv("WineQT.csv")
df = pd.DataFrame(data)

# print(df)

# 3. Analyze the data
'''print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.dtypes)'''

# 4. Checking Missing Values
'''print(df.isnull().sum())'''

# 5. Checking for duplicated values
# print(df.duplicated().sum())

# 6. Univariant Analysis
'''quality_counts = df["quality"].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(quality_counts.index, quality_counts.values, color="deeppink")
plt.xlabel("Quality")
plt.ylabel("Count")
plt.show()'''

'''sns.set_style("darkgrid")

numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

plt.figure(figsize=(8, len(numerical_columns) * 3))
for idx, feature in enumerate(numerical_columns, 1):
    plt.subplot(len(numerical_columns), 2, idx)
    sns.histplot(df[feature], kde=True)
    plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")

plt.tight_layout()
plt.show()
'''

'''plt.figure(figsize=(10, 8))

sns.swarmplot(x="quality", y="alcohol", data=df, palette="viridis")
plt.title("Swarm plot")
plt.xlabel("Quality")
plt.ylabel("Alcohol")
plt.show()'''

# Bivariate Analysis
'''avg_alcohol = df.groupby("quality")["alcohol"].mean()
# print(avg_alcohol)
plt.bar(avg_alcohol.index, avg_alcohol.values)
plt.title("Average Alcohol by Wine Quality")
plt.xlabel("Quality")
plt.ylabel("Average")
plt.show()'''

# Quality Vs Volatile Acidity
'''avg_volatileacidity = df.groupby("quality")["volatile acidity"].mean()
plt.bar(avg_volatileacidity.index, avg_volatileacidity.values)
plt.title("Quality vs Volatile Acidity")
plt.xlabel("Quality")
plt.ylabel("Volatile Acidity")
plt.show()'''

# Numerical vs Numerical Bivariate analysis
'''plt.scatter(df["quality"], df["alcohol"])
plt.xlabel("Quality")
plt.ylabel("Alcohol")
plt.title("Quality vs Alcohol")
plt.show()'''

'''correlation = df["alcohol"].corr(df["quality"])
print(correlation)'''

'''plt.scatter(df["quality"], df["volatile acidity"])
plt.title("Volatile acidity vs Quality")
plt.xlabel("Volatile Acidity")
plt.ylabel("Quality")
plt.show()

'''

'''correlation = df["volatile acidity"].corr(df["quality"])
print(correlation)'''

'''plt.scatter(df["quality"], df["sulphates"])
plt.title("Quality vs Sulphates")
plt.xlabel("Quality")
plt.ylabel("Sulphates")
plt.show()'''

'''correlation = df["sulphates"].corr(df["quality"])
print(correlation)'''

'''plt.scatter(df["quality"], df["citric acid"])
plt.title("Quality vs Citric acid")
plt.xlabel("Quality")
plt.ylabel("Citric Acid")
plt.show()'''

'''correlation = df["citric acid"].corr(df["quality"])
print(correlation)'''

'''plt.scatter(df["density"], df["alcohol"])
plt.title("Density vs Alcohol")
plt.xlabel("Density")
plt.ylabel("Alcohol")
plt.show()'''

'''correlation = df["alcohol"].corr(df["density"])
print(correlation)'''

correlation = df[
    [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "density",
        "pH",
        "sulphates",
        "alcohol",
        "quality"
    ]
].corr()

'''print(correlation)'''

# print(correlation["quality"].sort_values())

# Heatmap
'''import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,7))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)
plt.title("Wine Dataset Correlation Heatmap")
plt.show()'''

import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(
    df[[
            "fixed acidity",
            "volatile acidity",
            "citric acid",
            "residual sugar",
            "chlorides",
            "density",
            "pH",
            "sulphates",
            "alcohol",
            "quality"
        ]]
)
plt.show()