'''
Prefix and Suffix Sum

Geekoin50
Medium
Topics
Problem Statement:
Given a numbers N, print the sum of prefix sum and suffix sum array for each position.

Input Description:
Input Size : N <= 10000

Sample Input:
4
2 4 4 2

Sample Output:
14 16 16 14
'''
num = int(input())
nums = list(map(int, input().split()))
total= sum(nums)
sumlist = []
for n in nums:
    sumlist.append(total+n)
print(*sumlist)