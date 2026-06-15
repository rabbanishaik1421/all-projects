'''
Problem Statement:
Given a number N, print the sum of squares of all its digits.

Input Description:
The input consists of a number N, where 1 <= N <= 100000.

Output Description:
The output is the sum of squares of all digits of N.

Sample Input:
12

Sample Output:
5
'''
num = 12
num = str(num)
sum=0
for n in num:
    sum += int(n)*int(n)

print(sum) 