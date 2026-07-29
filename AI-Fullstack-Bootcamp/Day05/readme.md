# 🚀 AI/ML Engineer Roadmap - Day 05

## 📅 Date
> Add today's date here.

---

# 🎯 Day 05 Goal

Complete the remaining **Pandas** topics and begin the **NumPy** foundation.

---

# 📚 Topics to Complete

## ✅ Revision (20 Minutes)

Revise the following topics without referring to your notes.

- GroupBy
- Merge
- Concat
- Pivot Table
- Apply
- Drop vs Del
- loc vs iloc

---

# 📂 Pandas File Operations

## Read Files

Practice reading different file formats.

- read_csv()
- read_excel()
- read_json()

### Practice

- Read Employee CSV
- Read Employee Excel
- Read Employee JSON

---

## Write Files

Practice exporting DataFrames.

- to_csv()
- to_excel()
- to_json()

### Practice

Export the Employee DataFrame into:

- employees.csv
- employees.xlsx
- employees.json

Then read them back and compare:

- Shape
- Columns
- Data Types
-
---

# 📅 Date & Time

Learn and practice the following:

- pd.Timestamp()
- pd.Timestamp.now()
- pd.date_range()

Generate:

- Daily Dates
- Weekly Dates
- Monthly Dates
- Hourly Dates

Practice different frequencies.

```python
freq="D"   # Daily
freq="W"   # Weekly
freq="M"   # Monthly
freq="H"   # Hourly
```

---

# 📝 Notes to Prepare

Create notes for the following topics.

- read_csv()
- read_excel()
- read_json()
- to_csv()
- to_excel()
- to_json()
- Timestamp
- Date Range

Each topic should include:

- Definition
- Syntax
- Parameters
- Example
- Real-world Use Case
- Interview Question

---

# 🧮 NumPy Basics

Create a file:

```
numpy_basics.py
```

Practice:

```python
import numpy as np

arr = np.array([10,20,30,40,50])

print(arr)
print(type(arr))
print(arr.dtype)
print(arr.shape)
print(arr.ndim)
print(arr.size)
```

Understand:

- array()
- dtype
- shape
- ndim
- size

---

# ➕ NumPy Operations

Practice the following operations.

```python
arr + 10
arr - 5
arr * 2
arr / 2
arr ** 2
```

Compare these operations with Python Lists.

Answer:

> Why is NumPy faster than Python Lists?

---

# 💻 Mini Project

## Employee File Manager

### Menu

```
==================================
Employee File Manager
==================================

1. Display Employees
2. Export CSV
3. Export Excel
4. Export JSON
5. Read CSV
6. Read Excel
7. Read JSON
8. Generate Date Range
9. Display Current Timestamp
10. Exit
```

---

# 🧠 AI/ML Reading

Read the following topics.

- Why NumPy is important?
- Why is NumPy faster than Python Lists?
- Why do Pandas and Machine Learning libraries use NumPy?

Write a short summary in your notebook.

---

# 🎯 Interview Questions

Prepare answers for:

1. What is CSV?
2. Difference between CSV and Excel.
3. What is JSON?
4. Why do we use JSON?
5. What is read_csv()?
6. What is to_csv()?
7. What is Timestamp?
8. What is Date Range?
9. Why is NumPy faster than Python Lists?
10. What are the advantages of NumPy?

---

# 💡 Coding Challenge

Create the following DataFrame.

| Name | JoiningDate |
|------|-------------|
| Shaik | 2024-01-10 |
| Rabbani | 2024-03-15 |
| Harsha | 2023-11-01 |

Tasks:

- Convert JoiningDate into Datetime.
- Display Current Timestamp.
- Generate Date Range for the next 30 days.
- Find the Joining Month.
- Find the Joining Day Name.
- Calculate approximate Experience in Years.

---

# 📂 Folder Structure

```
Day05/
│
├── read_files.py
├── write_files.py
├── datetime_examples.py
├── numpy_basics.py
├── numpy_operations.py
├── employee_file_manager.py
├── notes.md
├── interview_questions.md
└── README.md
```

---

# 📈 Progress Tracker

| Module | Status |
|----------|--------|
| Python Fundamentals | ✅ Completed |
| Pandas Basics | ✅ Completed |
| DataFrame Operations | ✅ Completed |
| GroupBy | ✅ Completed |
| Merge | ✅ Completed |
| Concat | ✅ Completed |
| Pivot Table | ✅ Completed |
| File Operations | ⏳ In Progress |
| Date & Time | ⏳ In Progress |
| NumPy Basics | 🔜 Starting |
| Statistics | 🔜 Next |
| Data Visualization | 🔜 Upcoming |
| Machine Learning | 🔜 Upcoming |

---

# ✅ Day 05 Deliverables

- [ ] Revise Pandas concepts
- [ ] Practice read_csv()
- [ ] Practice read_excel()
- [ ] Practice read_json()
- [ ] Practice to_csv()
- [ ] Practice to_excel()
- [ ] Practice to_json()
- [ ] Complete Timestamp examples
- [ ] Complete Date Range examples
- [ ] Learn NumPy Basics
- [ ] Practice NumPy Operations
- [ ] Complete Employee File Manager Project
- [ ] Write Notes
- [ ] Prepare Interview Questions
- [ ] Push the code to GitHub

---

# 🌟 Quote of the Day

> **"Learning AI is not about finishing a course. It is about building the ability to solve real-world problems with data."**

---

# 🚀 Next Day Preview (Day 06)

Topics to Learn:

- NumPy Array Creation
- Array Indexing & Slicing
- NumPy Mathematical Functions
- Mean
- Median
- Mode
- Variance
- Standard Deviation
- Descriptive Statistics
- Practical Statistics Exercises