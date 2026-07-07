'''
158. Odd Digit Sum Check

Geekoin50
Medium
Topics
Solved!
Problem Statement:
A number is given as input. Find the odd digits in the number, add them and find if the sum is odd or not. If even print E, if odd print O.

Input Description:
Input Size : N <= 10000000000

Output Description:
If the sum of odd digits is even print E, if odd print O.

Sample Input:
413

Sample Output:
E
'''
num = str(input())
tot = 0
for i in num:
    tot +=int(i)
    
print("E" if tot % 2 == 0 else "O")