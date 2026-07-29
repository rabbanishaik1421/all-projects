import pandas as pd

# 1. Read the entire JSON file.
json = pd.read_json("anscombe.json")
# print(json)

# 2. Display descriptive statistics.
# print(json.describe())

# 3. Display missing values count.
# print(json.isnull().sum())

# 4. Display memory usage.
# print(json.memory_usage())

# 5. Read only the Series and Y columns.
# print(json[['Series', 'Y']])

# 6. Set Series as the index.
# print(json.set_index('Series'))

# 7.Display only Series "I".
# print(json[json["Series"] == 'I'])

# 8. Display only Series "II".
# print(json[json['Series'] == 'II'])

# 9.Display only rows where X > 10
# print(json[json['X']>10])

# 10. Find the average of column X.
# print(json[['X']].mean())

# 11. Count how many records belong to each Series.
print(json.groupby('Series').count())

