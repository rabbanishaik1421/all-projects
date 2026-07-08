#=============================================================#
#Group By Examples ====================================#
#=============================================================#
import pandas as pd

employees = {
    "EmpId":[101, 102, 103, 104, 105],
    "Name":["Shaik", "Rabbani", "Harsha", "Priya", "Madhu"],
    "Salary":[21000, 28000, 45000, 60000, 75000]
}

df = pd.DataFrame(employees)

#Add Column with value assignment
df["Country"] = "India"

#Add column with calculation
df["Bonus"] = df["Salary"] * 0.05

#Add a column with a list
df["Gender"] = ["Male", "Male", "Female", "Female", "Male"]

#Add Multiple columns
df["TaxAmount"] = df["Salary"] * 0.02
df["NetSalary"] = df["Salary"] - df["TaxAmount"]

df2 = df.assign(Bonus2=df["Salary"] * 0.05)

df.insert(3, "Department", ["IT", "IT", "HR", "HR", "Finance"])
# print(df)

def category(salary):
    if salary > 25000:
        return "Senior"
    else:
        return "Junior"

#using apply    
df["Category"] = df["Salary"].apply(category)

df.loc[:, "Experience"] = [3, 5, 6, 7, 8]

def change_country(experience):
    """
    Returns city based on experiece
    """
    if experience <= 3:
        return "Hyderabad"
    elif experience <= 5:
        return "Delhi"
    else:
        return "Bangalore"    

df["Country"] = df["Experience"].apply(change_country)

def performance(salary):
    """
    Returns performance report based on salary
    """
    if salary < 25000:
        return "Average"
    elif salary <= 50000:
        return "Good"
    else:
        return "Excellent"
    
df["Performance"] = df["Salary"].apply(performance)

print("Group By Employees Data")
# print(df)

#Country wise group by
# print(df.groupby("Country")[["Salary"]].mean())

#Department wise salary group by mean
print(df.groupby("Department")[["Salary"]].mean())