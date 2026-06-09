'''
Problem Statement:
Given a number N,K followed by array of N elements where the difference between any adjacent elements is 1. Find the position of the given number K.If K not found in the array print -1


Input Description:
The input consists of two integers N and K, followed by an array of N elements where the difference between any adjacent elements is 1.


Output Description:
The output is the position of the given number K. If K is not found in the array, print -1.


Sample Input:
5 1
3 2 1 2 3


Sample Output:
3
'''
n=5
k=1
nums = "3 2 1 2 3"
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

if k in nums:
    print(nums.index(k) + 1)
else:
    print(-1)