'''
98. Even Factors of a Number

Problem Statement:
Given a number N, print the even factors of N.If the even factor does not exists for N print '-1'.

Input Description:
Input Size : 1 <= N <= 1000

Sample Input:
8

Sample Output:
2 4 8
'''
num=2
num = int(num)
evenrange = []
for n in range(1,num+1):
    if num % n == 0 and n % 2 == 0:
        evenrange.append(n)

if evenrange:
    print(*evenrange)
else:
    print(-1)