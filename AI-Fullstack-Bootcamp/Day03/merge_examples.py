#Merge 
import pandas as pd

employee = pd.DataFrame({
    "EmpId":[101, 102, 103, 104, 105],
    "Name":["Shaik", "Rabbani", "Hello", "World", "Hi"]
})

salary = pd.DataFrame({
    "EmpId": [101, 102, 103, 104, 105],
    "Name":[50000, 65000, 45000, 75000, 60000]
})

# Inner Join
result = pd.merge(employee, salary, on="EmpId", how="inner")

# Left Join
result = pd.merge(employee, salary, on="EmpId", how="left")

# Right Join
result = pd.merge(employee, salary, on="EmpId", how="right")
print(result)