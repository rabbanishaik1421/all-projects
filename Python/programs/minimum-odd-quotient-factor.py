'''
Problem Statement:
Given number N, find the minimum factor which yeilds odd number as the quotient.


Input Description:
The input consists of a single integer N, where N <= 100000.


Output Description:
The output is the minimum factor of N that yields an odd number as the quotient.


Sample Input:
9


Sample Output:
1
'''
n=12
factor=1
while n%2 == 0:
    factor *= 2
    n//=2

print(factor)