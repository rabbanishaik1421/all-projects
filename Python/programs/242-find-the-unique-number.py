'''
242. Find the Unique Number

Given a number N followed by N numbers. All the numbers in the given input appear twice except for one number(ie one number appears only once in the given input). Find the number which appears only once.

Input Description:
The input consists of a number N, followed by N numbers. N is between 1 and 100000 (inclusive).

Output Description:
The output is the number that appears only once in the given input.

Sample Input:
5
1 2 1 3 2
'''
n=int(input())
nums = list(map(int, input().split()))
i=0
freq={}
while i<n:
    freq[nums[i]]=freq.get(nums[i], 0)+1
    i+=1
    
for k, v in freq.items():
    if v == 1:
        print(k)
        break