#=============================#
#==Group By functionality=====#
#=============================#
import pandas as pd

employees = {
    "Name":["Shaik", "Rabbani", "Harsha", "Priya", "Anjali", "Madhu"],
    "Salary": [25000, 67000, 50000, 45000, 35000, 90000]
}

df = pd.DataFrame(employees)
df["Department"] = ["IT", "HR", "Finance"] * 2
df["Location"] = ["Hyderabad", "Bangalore", "Delhi"] * 2
df["Bonus"] = df["Salary"] * 0.02
df["Age"] = [25] * 6

#====================================#
#Department wise salary report=======#
#====================================#
def department_salary_report(df):
    department_report = df.groupby(["Department"])["Salary"].agg(
        EmployeeCount = "count", 
        TotalSalary = "sum", 
        AverageSalary = "mean", 
        HighestSalary = "max", 
        LowestSalary = "min"
    )

    return department_report

report = department_salary_report(df)

#Transform
df["AverageSalary"] = df.groupby("Department")["Salary"].transform("mean")

#filter
result = df.groupby("Department").filter(lambda x: x["Salary"].mean() > 50000)
# print(result)

#value counts
counts = df.value_counts("Department")
# print(counts)

#Sort Data Frame
dfresult = df.sort_values(by="Salary", ascending=True)
print(dfresult)

