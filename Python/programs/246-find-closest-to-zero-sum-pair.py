'''
246. Find Closest to Zero Sum Pair

Problem Statement:
Given an array of size N with both positive and negative numbers. Find two elements such that their sum is equal or closest to zero.

Input Description:
Input Size : 1 <= N <= 100000

Sample Input:
5
-1 2 3 1 0

Sample Output:
1 -1
'''
n=5
nums = "-1 2 3 1 0"

n=5
nums = "-1 2 2 3 7"

n=5
nums="-2 -3 0 5 1"

nums = list(map(int, nums.split()))
nums = sorted(nums)
numindex = nums.index(0)
print(nums[numindex-1], nums[numindex+1])