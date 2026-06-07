'''
Problem Statement:
Given a number N, print the sum of the squares of its digits.


Input Description:
The input consists of a number N, where 1 <= N <= 1000000000000000000.


Output Description:
The output is the sum of the squares of the digits of N.

Sample Input:
19

Sample Output:
82
'''
num="19"
result = 0
for i in num:
    i = int(i)
    result += i * i

print(result)

