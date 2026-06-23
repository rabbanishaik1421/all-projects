'''
212. Sum of Negative Numbers

Problem Statement:
Given a number N and an array of N integers, find the sum of all the negative numbers in the array.

Input Description:
The input consists of an integer N, followed by N integers. N is less than or equal to 100000.

Sample Input:
2
3 0

Sample Output:
0
'''
n=2
nums = "3 0"
nums = "3 -1"
nums = list(map(int, nums.split()))
i=0
total=0
while i<n:
    if nums[i] < 0:
        total += nums[i]
    i+=1

print(total)
