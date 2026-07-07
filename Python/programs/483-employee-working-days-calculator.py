'''
Problem Statement:
In a firm there is an intelligent employee. He said that he will not work on all those days which has factors more than 2. You are given with month and year calculate the no of working days of employee.

Input Description:
Month(M) and year(Y)

Output Description:
N denoting no of working days

Explanation:
2,3,5,7,11,13,17,19,23,19,31 are the days on which he will work.

Sample Input:
May 2016

Sample Output:
11
'''
import calendar

# Input: Month Year (e.g., May 2016)
month_name, year = input().split()
year = int(year)

# Convert month name to month number
month = list(calendar.month_name).index(month_name)

# Get number of days in the month
days = calendar.monthrange(year, month)[1]

# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Count prime dates
count = 0
for day in range(1, days + 1):
    if is_prime(day):
        count += 1

print(count)