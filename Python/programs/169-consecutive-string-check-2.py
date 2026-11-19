'''
169. Consecutive String Check-2

Problem Statement:
Given 2 numbers N,K and an array of N strings, find if any K consecutive strings are same.

Input Description:
Input Size : K <= N <= 1000

Sample Input:
5 3
code
overload
vishal
vishal
vishal

Sample Output:
yes
'''
n, k = map(int, input().split())
strings = [input().strip() for _ in range(n)]

count = 1
found = "no"

if k == 1 and n >= 1:
    found = "yes"
else:
    for i in range(1, n):
        if strings[i] == strings[i - 1]:
            count += 1
            if count == k:
                found = "yes"
                break
        else:
            count = 1

print(found)