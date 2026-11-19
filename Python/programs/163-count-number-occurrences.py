'''
Problem Statement:
Given an array of numbers and another number k. Find whether K exists and the number of time k repeats. If it does not exist just print no.

Input Description:
Input Size : |N| <= 1000000

Sample Input:
5 3
3 3 4 4 7

Sample Output:
yes 2
'''
nums = "3 3 4 4 7"
k = 3
count = 0
nums = list(map(int, nums.split()))
for n in nums:
    if k == n:
        count = count + 1
if count>1:
    print("yes", count)
