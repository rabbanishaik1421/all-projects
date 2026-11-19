'''
Problem Statement:
Given a number n and 2 numbers l and r followed by n numbers, find the smallest number in the range [l,r].

Input Description:
The input consists of an integer n, two integers l and r, followed by n integers.

Output Description:
The output is the smallest number found within the specified range [l,r].

Sample Input:
5 2 4
1 2 3 4 5

Sample Output:
2
'''
n=5
l=2
r=4
num = [1, 2, 3, 4, 5]
num = [1, 1, 1, 1, 1, 1]
minarr = []
for i in range(l, r+1):
    if i in num:
        minarr.append(i)

if minarr:
    print(min(minarr))
else:
    print(-1)