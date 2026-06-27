'''
137. Prefix Sum Array

Problem Statement:
Given a number N and an array of N elements, print the prefix sum array.

Input Description:
Input Size : N <= 100000

Output Description:
The output is the prefix sum array.

Sample Input:
4
2 4 4 2

Sample Output:
2 6 10 12
'''
n = int(input())
nums = list(map(int, input().split()))
newnums = []
newnum = 0
i=0
while i<len(nums):
    newnum += nums[i]
    newnums.append(newnum)
    i+=1

print(*newnums)