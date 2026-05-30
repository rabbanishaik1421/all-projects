'''
30. Nearest Greater Multiple of 10

Geekoin20
Easy
Topics
Problem Statement:
Given a number N, find the nearest greater multiple of 10.


Input Description:
Input Size : N <= 10000


Sample Input:
3


Sample Output:
10

'''
n = 9
if n % 10 == 0:
    print(n)
else:
    d = n //2
    print((d+1) * 10)