'''
Problem Statement:
Given 2 numbers N,K followed by N elements print all the elements lesser than K in sorted order.If the elements could not be found print -1


Input Description:
Input Size : N <= 100000


Sample Input:
5 3 1 2 1 4 1


Sample Output:
1 1 1 2
'''
N, K = 5, 2
nums = "1 2 4 1 1"
nums = list(map(int, nums.split()))
newnums = []
for i in range(N):
    if nums[i] < 2:
        newnums.append(nums[i])

print(*newnums)