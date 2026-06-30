'''
Problem Statement:
You are provided with a number, "N". Find its factorial.

Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Explanation:
2! = 2*1 = 2

Sample Input:
2

Sample Output:
2
'''
n = int(input())
factorial = 1
for i in range(1,n+1):
    factorial *=i

print(factorial)