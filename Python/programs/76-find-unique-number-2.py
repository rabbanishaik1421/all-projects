'''
Problem Statement:
Given a number N and an array of N elements, every number is repeated except for one. Print that one number.


Input Description:
Input Size : 1 <= N <= 100000


Sample Input:
10
1 2 3 2 3 3 2 5 5 2


Sample Output:
1
'''
nums = "1 2 3 2 3 3 2 5 5 2"
nums = list(map(int, nums.split()))
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0)+1

values = freq.values()
minval = min(values)
print(minval)
