import kagglehub
import pandas as pd
import os
import random
import numpy as np

# Download latest version
path = kagglehub.dataset_download("tawfikelmetwally/employee-dataset")

# emp_data = pd.read_csv(path+"Employee.csv")
emp_data = pd.read_csv(os.path.join(path, "Employee.csv"))
# print(emp_data)

# 1. Display first and last records
# print("Top Rows: \n", emp_data.head(10))
# print("Bottom Rows: \n", emp_data.tail(10))

# 2.Check shape, columns, and data types
# print("Shape:\n", emp_data.shape)
# print("Columns:\n", emp_data.columns)
# print("Data Types:\n", emp_data.dtypes)

# 3.Display summary statistics
# print("Summarize Statistics:\n", emp_data.describe())

# 4.Select specific columns
# print("Specific Columns:\n", emp_data[["Education", "JoiningYear", "Age", "Gender"]])
# print("Loc:\n",emp_data.loc[2, "Education"])
# print("iloc:\n", emp_data.iloc[[1,3], [0, 2]])

# 5.Set EmpID as the index
# print("Set EmpID Index:\n", emp_data.set_index("Education"))

# 6.reset index
# print("Reset Index:", emp_data.reset_index(inplace=True))

# 7.Joining Year > 2015
# print("Employees with salary > 50,000\n", emp_data[emp_data["JoiningYear"]>2016])

# 8.Education Bachelors list
# print(emp_data[emp_data["Education"]=='Bachelors'])

# 9.Employees with age > 25
# print("Employees with salary > 50,000\n", emp_data[emp_data["Age"]>25])

# 10.Employees from Pune
# print(emp_data[emp_data["City"]=='Pune'])

# 11. Add Salary
emp_data["Salary"] = [random.randint(10000, 50000) for _ in range(len(emp_data))]

# 12. Increase salary by 10%
emp_data["Salary"] = emp_data["Salary"] * 1.10

# 13. Create a Bonus column 10% 
emp_data["Bonus"] = emp_data["Salary"] * 0.10

# 14. Create a Tax column
emp_data["Tax"] = emp_data["Salary"] * 0.20

# 15.Create a NetSalary column
emp_data["NetSalary"] = emp_data["Salary"] + emp_data["Bonus"] - emp_data["Tax"]

# Create a Performance column
def performance(salary):
    if salary>65000:
        return "Best"
    elif salary>50000:
        return "Good"
    else:
        return "Better"

emp_data["Performance"] = emp_data["Salary"].apply(performance)

# 16.Sort by salary
# print(emp_data.sort_values('Salary', ascending=False))

# 17. Sort by experience
emp_data['Experience'] = [random.randint(1, 5) for _ in range(len(emp_data))]

# 18. Add Department
departments = ["HR", "IT", "Finance", "Sales", "Marketing", "Operations"]

emp_data["Department"] = np.random.choice(
    departments,
    size=len(emp_data)
)
# 19.Sort by experience
# print(emp_data.sort_values(["Department", "Salary"], ascending=False))

# 20.Average salary by department
print("Average Salary:\n========================\n",emp_data.groupby('Department')['Salary'].mean())

# 21.Maximum salary by department
print("Maximum Salary:\n========================\n", emp_data.groupby('Department')['Salary'].max())

# 22.Employee count by department
print("Department Count:\n========================\n", emp_data.groupby('Department')['Salary'].count())

# 23. Introduce missing values
emp_data.loc[2, "Salary"] = np.nan
emp_data.loc[5, "Department"] = np.nan
emp_data.loc[8, "Age"] = np.nan

# 24. Fill missing values
emp_data["Salary"] = emp_data["Salary"].fillna(
    emp_data["Salary"].mean()
)

# 25. Detect missing values
print("Missing values", emp_data.isnull().sum())

