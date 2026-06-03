'''
Problem Statement:
Given a number N and an array of N elements, find the length of the longest repeating sequence of the elements.If no such sequence is found print -1


Input Description:
The input consists of an integer N (where N <= 100000) and an array of N elements.


Sample Input:
8
1 2 2 2 3 4 5 6


Sample Output:
3
'''

n=8
nums = "1 2 2 2 3 4 5 6"
nums = list(map(int, nums.split()))

freq={}
for i in nums:
    freq[i]=freq.get(i,0)+1

values = freq.values()
print(max(set(values)))