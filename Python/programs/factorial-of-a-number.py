'''
48. Factorial of a Number-2

Problem Statement:
Given a number N, find the factorial of N.


Input Description:
The input consists of a single integer N, constrained by 1 <= N <= 25.


Output Description:
The output is the calculated factorial of N.


Sample Input:
5


Sample Output:
120
'''

def factorial(num):
    factorial=1
    for n in range(1, num + 1):
        factorial *=n
    return factorial

num=6
print(factorial(num))
