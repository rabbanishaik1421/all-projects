'''
113. Max Bitwise OR of Segments

Problem Statement:
Given a number N and an array of N integers, find the maximum of Bitwise OR of all segments.

Input Description:
Input Size : N <= 100000

Sample Input:
2
2 4

Sample Output:
6
'''

n = 2
nums = "2 4"
arr = list(map(int, nums.split()))

result = 0
for num in arr:
    result |=num

print(result)
