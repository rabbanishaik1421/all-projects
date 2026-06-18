'''
120. Decimal to Binary Conversion

Problem Statement:
Given a number N in decimal convert it into binary value.

Input Description:
Input Size : N <= 100000

Sample Input:
5

Sample Output:
101
'''
n=5
result = bin(n)[2:]
print(result)