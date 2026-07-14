'''
Problem Statement:
Accept a string and find if it is of date format 'dd/mm/yyyy'.

Sample Input:
01/13/1999

Sample Output:
no
'''
date = input()

parts = date.split('/')

if len(parts) != 3:
    print("no")
else:
    day, month, year = parts

    if (len(day) == 2 and
        len(month) == 2 and
        len(year) == 4 and
        day.isdigit() and
        month.isdigit() and
        year.isdigit()):

        day = int(day)
        month = int(month)
        year = int(year)

        if 1 <= month <= 12:

            # Days in each month
            days = [31,28,31,30,31,30,31,31,30,31,30,31]

            # Leap year
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                days[1] = 29

            if 1 <= day <= days[month-1]:
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        print("no")