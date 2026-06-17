'''
109. Integer or Long

Problem Statement:
Given a number N, print 'INT' if it is integer range or print 'LONG' if it is greater.

Input Description:
Input Size : 1 <= N <= 100000

Sample Input:
999

Sample Output:
INT
'''
num = 999

if len(str(num)) > 6:
    print("LONG")
else:
    print("INT")