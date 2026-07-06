# Import the Pandas library
import pandas as pd

# ---------------------------
# Series
# ---------------------------

# Create a Series from a Python list
data = [40, 78, 76, 64, 34, 25]
ds = pd.Series(data)

# Print the Series
# print(ds)

# ---------------------------
# DataFrame
# ---------------------------

# Create a dictionary containing student data
students = {
    "Name": ["Shaik", "Rabbani", "Harsha", "Anjali", "Vivek", "Gautami"],
    "Marks": [75, 79, 85, 90, 76, 82]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(students)

print("DataFrame")
print(df)

# ---------------------------
# head()
# ---------------------------

# Display the first 2 rows of the DataFrame
print("\nHead")
print(df.head(2))

# ---------------------------
# tail()
# ---------------------------

# Display the last 2 rows of the DataFrame
print("\nTail")
print(df.tail(2))

# ---------------------------
# shape
# ---------------------------

# Returns the number of rows and columns as a tuple (rows, columns)
print("\nShape")
print(df.shape)

# ---------------------------
# columns
# ---------------------------

# Returns the column names (Index object)
print("\nColumns")
print(df.columns)

# ---------------------------
# info()
# ---------------------------

print("\nDataFrame Information")

# Displays summary information such as:
# - Number of rows
# - Column names
# - Data types
# - Non-null values
# - Memory usage
df.info()

# ---------------------------
# describe()
# ---------------------------

# Generates descriptive statistics for numeric columns
# It returns:
# Count
# Mean
# Standard Deviation
# Minimum
# 25th Percentile
# 50th Percentile (Median)
# 75th Percentile
# Maximum

print("\nDescribe")
print(df.describe())