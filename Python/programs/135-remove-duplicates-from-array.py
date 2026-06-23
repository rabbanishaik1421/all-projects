'''
135. Remove Duplicates from Array

Problem Statement:
Given a number N and an array of N elements, print the array after removing duplicate elements.If no duplicate elements found print the same.

Input Description:
Input Size : N <= 100000

Sample Input:
4
2 4 4 2

Sample Output:
2 4
'''
n=4
nums = "2 4 4 2"
nums = "1 2 3 4"
nums = list(map(int, nums.split()))
i=0
nonduparr = []
while i<n:
    if nums[i] not in nonduparr:
        nonduparr.append(nums[i])
        #print(nums[i])
    i+=1

print(*nonduparr)