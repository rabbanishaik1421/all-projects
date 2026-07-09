import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 21, 22, 23]
}

df = pd.DataFrame(data, index=["S1", "S2", "S3", "S4"])

# print(df)
# print(df.loc["S3"])
# print(df.iloc[2])
# print(df.loc["S2", "Age"])
print(df.iloc[1, 1])