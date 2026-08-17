import pandas as pd
import matplotlib as plt

employees = [
    {
        "name":"Shaik",
        "salary":25000,
        "department":"IT"
    },
    {
        "name":"Rabbani",
        "salary":30000,
        "department":"IT"   
    },
    {
        "name":"Harsha",
        "salary":32000,
        "department":"IT"   
    },
    {
        "name":"Anjali",
        "salary":35000,
        "department":"IT"   
    },
    {
        "name":"Chandrika",
        "salary":38000,
        "department":"IT"   
    }
]

df = pd.DataFrame(employees)
print(df)