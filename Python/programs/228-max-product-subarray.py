'''
228. Max Product Subarray

Problem Statement:
Given a number N and an array of size N(with both positive and negative integers), print the product of the elements in the maximum product subarray.

Input Description:
The input consists of a number N and an array of size N with both positive and negative integers. N is between 1 and 100000 (inclusive).

Output Description:
The output is the product of the elements in the maximum product subarray.

Sample Input:
5
1 2 3 4 5

Sample Output:
120
'''
n=5
nums = "1 2 3 4 5"
n=10
nums = "1 2 3 4 -100 6 -21 7 -1 8"
nums = list(map(int, nums.split()))

if n == len(nums):
    prod = 1
    for i in nums:
        prod *=i

    print(prod)
else:
    print(-1)