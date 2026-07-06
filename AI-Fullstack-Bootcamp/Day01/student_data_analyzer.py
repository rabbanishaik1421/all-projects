#--------------------------------
# Student Data Analyzer
# 1.Total Students

# 2.Highest Marks

# 3.Lowest Marks

# 4.Average Marks

# 5.Display Dataset

# 6.Exit
#--------------------------------

#Import Pandas for Data Manipulation and Data Analysis
import pandas as pd

#Read the students data from the students.csv
students = pd.read_csv("students.csv")

#--------------------------------
# Total Students Function
#--------------------------------
def total_students():
    totalStudents = len(students)
    return totalStudents

#--------------------------------
# Highest Marks Calculate Function
#--------------------------------
def highest_marks():
    highmarks = students["Marks"].max()
    return highmarks

#--------------------------------
# Lowest Marks Calculate Function
#--------------------------------
def lowest_marks():
    lowmarks = students["Marks"].min()
    return lowmarks

#--------------------------------
# Average Marks Calculate Function
#--------------------------------
def average_marks():
    avgmarks = students["Marks"].mean()
    return avgmarks

#--------------------------------
# Display Students Function
#--------------------------------
def display_students():
    return students

while True:
    print("Student Analyzer:")
    print("=======================================")
    print("1. Total Students")
    print("2. Highest Marks")
    print("3. Lowest Marks")
    print("4. Average Marks")
    print("5. Display Dataset")
    print("6. Exit")
    
    choice = int(input("Enter your choice:"))

    #Total Students function call
    if choice == 1:
        totalStudents = total_students()
        print("Total Students:", totalStudents)
        break

    elif choice == 2:
        highestMarks = highest_marks()
        print("Highest Marks", highestMarks)
        break

    elif choice == 3:
        lowestMarks = lowest_marks()
        print("Lowest Marks", lowestMarks)
        break

    elif choice == 4:
        avgMarks = average_marks()
        print("Average Marks", avgMarks)
        break

    elif choice == 5:
        dispStudents = display_students()
        print("Students List:")
        print(students)
        break

    elif choice == 6:
        print("Thank you, See you again!")
        break
