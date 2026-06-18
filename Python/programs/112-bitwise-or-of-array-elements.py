'''
112. Bitwise OR of Array Elements

Company
Problem Statement:
Given a number N and an array of N elements, find the Bitwise OR of the array elements.

Input Description:
Input Size : N <= 100000

Output Description:
The output is the Bitwise OR of the array elements.

Sample Input:
2
2 4

Sample Output:
6
'''
n = 4
nums = "4 3 2 1"
arr = list(map(int, nums.split()))

result = arr[0]

for i in range(1, n):
    result |= arr[i]

print(result)
