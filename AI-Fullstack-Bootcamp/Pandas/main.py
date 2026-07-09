import pandas as pd

sensor_data ={
    "sensor1" : list(range(1, 11)),
    "sensor2" : [x ** 2 for x in range(1, 11)],
    "sensor3" : [x ** 3 for x in range(1, 11)],
    "sensor4" : ["entry_"+str(x) for x in range(1, 11)]
}

df = pd.DataFrame(sensor_data)
#print(df)

#Search Column
#print(df["sensor4"])

#Search row
#print(df.iloc[6])

#selecting a single cell
# print(df.iloc[6]["sensor3"])
# print(df["sensor3"][6])

#Get information
# print(df.info())

#Describe
# print(df.describe())

#Means
# print(df["sensor1"].mean())

# print(df[["sensor3","sensor1"]])

#Rows
# print(df.iloc[[4, 3, 8]])

#Row + columns
# print(df.iloc[[4,3,8]][["sensor3", "sensor1"]])

#row slicing
print(df[3:8:2])