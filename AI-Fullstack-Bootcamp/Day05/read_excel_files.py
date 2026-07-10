import pandas as pd

#1. Read Excel
housing_test = pd.read_excel("california_housing_test.xlsx", sheet_name="california_housing_test")
# print(housing_test)

# 2. Display the first 5 rows.
# print(housing_test.head(5))

# 3. Display the last 10 rows.
# print(housing_test.tail(10))

# 4. Display the shape of the DataFrame.
# print(housing_test.shape)
# rows, cols = housing_test.shape
# print("Rows: ", rows, "Cols: ", cols)

# 5. Display all column names.
# print(housing_test.columns)

# 6. Display the data types of all columns
# print(housing_test.dtypes)

# 7. Display descriptive statistics using describe().
# print(housing_test.describe())

# 8. Display DataFrame information using info().
# print(housing_test.info())

# 9. Read only the first 100 rows.
# print(housing_test.nrows(100))
numrows = pd.read_excel(
    "california_housing_test.xlsx", 
    sheet_name="california_housing_test",
    nrows=100
)
# print(numrows)

# 10. Skip the first 5 rows while reading.
skip_rows = pd.read_excel(
    "california_housing_test.xlsx", 
    sheet_name="california_housing_test",
    skiprows=100
)
# print(skip_rows)

'''11. Read only the following columns:
longitude
latitude
median_income'''
# print(pd.read_excel(
#     "california_housing_test.xlsx", 
#     sheet_name="california_housing_test",
#     usecols=["longitude", "latitude", "total_rooms"]
# ))

# 12. Read columns A:D using Excel column letters.
# print(pd.read_excel(
#     "california_housing_test.xlsx", 
#     sheet_name="california_housing_test",
#     usecols="A:D"
# ))

# 13. Set longitude as the index column while reading.
# print(pd.read_excel(
#     "california_housing_test.xlsx", 
#     sheet_name="california_housing_test",
#     index_col="longitude"
# ))

# 14. Rename all columns while reading the Excel file.
# print(pd.read_excel(
#     "california_housing_test.xlsx", 
#     sheet_name="california_housing_test",
#     header=0,
#     names=["Longitude", "Latitude", "Housing Median Age", "Total Rooms", "Total Bedrooms", "Population", "House Holds", "Median Income", "Median House Value"]
# ))

# 17. Read multiple worksheets together.
print(pd.read_excel(
    "california_housing_test.xlsx", 
    sheet_name=["california_housing_test", "sheet2"],    
))