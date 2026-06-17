'''
108. Odd Factors of a Number

Problem Statement:
Given a number N, print the odd factors for the N.

Input Description:
The input consists of a single integer N, where 1 <= N <= 1000.

Sample Input:
9

Sample Output:
1 3 9
'''
num=9
num = int(input())
oddfactors = []
for n in range(1, num+1):
    if num % n == 0 and n % 2 != 0:
        oddfactors.append(n)

print(*oddfactors)