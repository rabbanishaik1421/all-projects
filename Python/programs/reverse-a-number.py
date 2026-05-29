'''
Problem Statement:
Given a number N, print its reverse.


Input Description:
Input Size : n <= 1000


Sample Input:
10


Sample Output:
1
'''

n=987
numstr = str(n)
revstr = numstr[::-1]
revnum = int(revstr)
print(revnum)