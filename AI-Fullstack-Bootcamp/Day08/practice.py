import matplotlib.pyplot as plt

import pandas as pd

employees = {
    "EmpId": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    
    "Name": [
        "Shaik", "Rabbani", "Harsha", "Priya", "Madhu",
        "Anjali", "Vivek", "Kiran", "Suresh", "Gautami"
    ],
    
    "Department": [
        "IT", "IT", "HR", "HR", "Finance",
        "Finance", "IT", "Sales", "Sales", "IT"
    ],
    
    "Gender": [
        "Male", "Male", "Male", "Female", "Male",
        "Female", "Male", "Male", "Male", "Female"
    ],
    
    "Experience": [
        1, 3, 5, 7, 10, 2, 6, 4, 8, 9
    ],
    
    "Salary": [
        25000, 35000, 45000, 55000, 70000,
        30000, 50000, 40000, 60000, 65000
    ],
    
    "Age": [
        22, 25, 28, 32, 38,
        24, 30, 27, 35, 36
    ]
}

df = pd.DataFrame(employees)

# print(df)
# Bar Chart Employee VS Salary
'''plt.bar(df["Name"], df["Salary"])
plt.title("Employee vs salary Bar Chart")
plt.xlabel("Employee Name")
plt.ylabel("Employee Salary")
plt.grid(axis="y")
plt.show()
'''

# Line Chart - Employee vs Salary
'''plt.plot(df["Name"], df["Salary"])
plt.title("Employee vs salary Line Chart")
plt.xlabel("Employee Name")
plt.ylabel("Employee Salary")
plt.show()'''

# Horizonatal Bar
'''plt.barh(df["Name"], df["Salary"])
plt.title("Employee vs Salary Horizontal Bar")
plt.xlabel("Employee Name")
plt.ylabel("Employee Salary")
plt.show()'''

# Scatter Plot
# plt.scatter(df["Name"], df["Salary"])
# plt.title("Employee vs Salary Scatter Plot")
# plt.xlabel("Employee")
# plt.ylabel("Salary")
# plt.grid(axis="y")
# plt.show()

# Scatter Plot
# plt.scatter(df["Age"], df["Salary"])
# plt.title("Age vs Salary scatter plot")
# plt.xlabel('Age')
# plt.ylabel("Salary")
# plt.grid(axis="both")
# plt.show()

# Historgram
# plt.hist(df["Salary"], bins=10)
# plt.title("Salary Distribution")
# plt.show()

# Categorical Data - Department
# department_data = df["Department"].value_counts()
# plt.bar(department_data.index, department_data.values)
# plt.title("Categorical Data - Bar Chart")
# plt.xlabel("Department Name")
# plt.ylabel("Department Values")
# plt.grid(axis="y")
# plt.show()

# Categorical Data - Pie Chart
'''gender_data = df["Gender"].value_counts()
plt.pie(
    gender_data.values,
    labels=gender_data.index,
    autopct="%1.1f%%"
)
plt.show()'''

# Salary vs Experience
'''plt.scatter(df["Salary"], df["Experience"])
plt.xlabel("Salary")
plt.ylabel("Experience")
plt.show()'''

