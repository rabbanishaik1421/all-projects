'''
101. Power of a Number

Problem Statement:
Given 2 numbers N and K.check if N is a power of K.Print 'yes' if it is a power of k otherwise print 'no'.

Sample Input:
64 8

Sample Output:
yes
'''
nums = "64 8"
n, k = list(map(int, input().split()))

power=1
while power<n:
    power *=k

if power == n:
    print('yes')
else:
    print('no')