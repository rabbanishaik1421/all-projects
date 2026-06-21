'''
125. Sum of First and Last Digits

Problem Statement:
Given a number N, print the sum of its first and last digit.

Input Description:
Input Size : |N| <= 10000

Sample Input:
51233

Sample Output:
8
'''
num = 51233
num = 1220
num = 1321
num = str(num)
numlen = len(num)
sum = int(num[0]) + int(num[numlen-1] )
print(sum)
