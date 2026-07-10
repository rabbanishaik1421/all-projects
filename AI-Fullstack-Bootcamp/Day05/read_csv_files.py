import pandas as pd

#1. Read the entire CSV file.
housing_test = pd.read_csv("california_housing_test.csv")
print(housing_test)

# 2. Display only the first 5 rows.
top_rows = housing_test.head(5)
print(top_rows)

# 3. Display only the last 10 rows.
last_records = housing_test.tail(10)
print(last_records)

# 4. Disply the shape.
shaperec = housing_test.shape
print(shaperec)

# 5. Display column names.
column_names = housing_test.columns
print(column_names)

# 6. Display data types.
data_types = housing_test.dtypes
print(data_types)

# 7. Display descriptive statistics.
print(housing_test.describe())

#8 Read only longitude, latitude, and median_income.
# print(housing_test.columns('longitude', 'latitude', 'median_income'))
housing_test_columns = housing_test[['longitude', 'latitude', 'median_income']]
print(housing_test_columns)

#9 Set longitude as the index
hs = housing_test.set_index('longitude')
print(hs)

#10 Read in chunks of 500 rows.
chunks = pd.read_csv(
    "california_housing_test.csv",
    chunksize=50
)

for chunk in chunks:
    print(chunk)

#11 Find the average median_house_value.
print("Average mediann house value: ", housing_test['median_house_value'].mean())

# 12. Find the house with the maximum value.
print("Maximum house value:", housing_test['median_house_value'].max())

#13. Filter houses where median_income > 5
print("Filter Houses:", housing_test[housing_test['median_income']>5])

#14. Sort by median_house_value.
print(housing_test.sort_values('median_house_value'))

#15. Create a pivot table using another categorical column (after creating one)

#16 Display random rows
housing_test.sample(5)

#17 Display unique values
housing_test['housing_median_age'].unique()

#18 Count unique values
print(housing_test.nunique())