'''
768. Leap Year Check-2

Problem Statement:
Let "A" be a year, write a program to check whether this year is a leap year or not. Print "Y" if its a leap year and "N" if its a common year.

Input Description:
A Year is the input in the form of a positive integer.

Output Description:
Print "Y" if its a leap year and "N" if its a common year.

Sample Input:
2020

Sample Output:
Y

Explanation:
2020 is a leap year.
'''
n = int(input())
if n % 4 == 0:
    print("Y")
else:
    print("N")