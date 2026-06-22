'''
134. Sort and Print Original Indices

Problem Statement:
Given a number N and an array of N elements,sort the array in increasing order and print the original indices of the elements present in sorted array.

Input Description:
Input Size : N <= 100000

Sample Input:
5
5 4 3 2 1

Sample Output:
5 4 3 2 1
'''
nums = "5 4 3 2 1"
nums = list(map(int, nums.split()))
nums = sorted(nums, reverse=True)
print(nums)