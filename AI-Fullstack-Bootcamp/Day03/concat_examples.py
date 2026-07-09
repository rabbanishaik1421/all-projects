import pandas as pd

df1 = pd.DataFrame({
    "Name":["Hello", "Rabbani"]
})

df2 = pd.DataFrame({
    "Name":["Hello", "World"]
})

# result = pd.concat([df1, df2])

# result = pd.concat([df1, df2], ignore_index=True)

# result = pd.concat([df1, df2], axis=1)

# result = pd.concat([df1, df2], axis=0)

# Outer Join
# result = pd.concat([df1, df2], join="outer")

#Inner join
result = pd.concat([df1, df2], join="inner")

print(result)