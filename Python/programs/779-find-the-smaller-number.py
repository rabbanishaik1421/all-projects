'''
Problem Statement:
You are provided with two numbers. Find and print the smaller number.

Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input:
23 1

Sample Output:
1

Explanation:
1 < 23
'''
nums = list(map(int, input().split()))
minval = min(nums)
print(minval)