import pandas as pd

# 1. Read the California Housing dataset and save it as a CSV without the index.
df = pd.read_csv("california_housing_test.csv")
df.to_csv(
    "housing_clean.csv",
    index=False
)

# 2. Save only the following columns:
'''longitude
latitude
median_income
median_house_value
'''
# df_columns = df[["longitude", "latitude", "median_income", "median_house_value"]]
# df_columns.to_csv(
#     "test.csv"
# )

# 3. Save only houses where:
# high_income_houses = df[df["median_income"] > 15]
# high_income_houses.to_csv(
#     "test.csv",
#     index=False
# )

# 4. Save houses sorted by median_house_value (highest first).
# sortedvalues = df.sort_values(by="median_house_value", ascending=False)
# sortedvalues.to_csv(
#     "test.csv",
#     index=False
# )

# 5. Remove duplicate rows (if any) and save the cleaned dataset.
# df_duplicates = df.drop_duplicates()
# df_duplicates.to_csv(
#     "test.csv",
#     index=False
# )

# 6. Export the complete DataFrame to Excel.
# df.to_excel("test.xlsx", index=False)

# 7. Export only the first 100 rows.
# df.head(100).to_excel("test.xlsx", index=False)

# 8. Export houses having:
df[df["median_house_value"] > 250000].to_excel("PremiumHouses.xlsx", index=False)

# 9. Create two worksheets. using ExcelWriter

# 10. Export only selected columns into Excel.
'''
Columns:
median_income
population
households
'''
# df[["median_income", "population", "households"]].to_excel("test.xlsx", index=False)

# 11. Save the complete DataFrame into JSON.
# df.to_json("test.json", orient='records')

# 12. Save JSON with indentation.
# df.to_json("test.json", indent=4)

# 13. Save only houses having:
# df[df['median_income']>6].to_json("test.json", orient='records')

# 14. Save only the first 20 rows into JSON.
df.head(20).to_json("test.json", orient="records")

# 15. Save JSON Lines.
# df.to_json("test.json", orient="records", lines=True)

def income_level(income):
    if income>6:
        return 'High';
    elif income > 3:
        return 'Medium'
    elif income < 3:
        return 'Low'
    else:
        return ''
    
df["Income_Level"] = df['median_income'].apply(income_level)
# print(df)

# 16. Export only High Income houses.
# df[df['Income_Level'] == 'Medium'].to_excel("test.xlsx", index=True)

# 17. Export only Medium Income houses.
# df[df['Income_Level'] == 'High'].to_csv('test.csv', index=True)

# 18. Export only Low Income houses.
# df[df['Income_Level'] == 'Low'].to_json('test.json', indent=4)

# 19. Create a pivot table.
# pivot_table = pd.pivot_table(
#     df,
#     values='median_house_value',
#     index="Income_Level",
#     aggfunc="mean",
#     dropna=True
# )
# pivot_table.to_excel("test.xlsx", index=True)

# 22. Remove unnecessary columns.
# df_clean = df.drop(
#     columns=[
#         "longitude",
#         "latitude"
#     ]
# ).to_csv("test.csv", index=True)


