'''
130. Max Sum of Adjacent Pairs

Problem Statement:
Given a number N and an array of N elements, find the sum of the maximum elements obtained by considering all consecutive pairs of adjacent elements.

Input Description:
The input consists of a number N representing the size of the array, followed by N elements. N <= 100000.

Sample Input:
5
1 2 3 4 5

Sample Output:
14
'''
n=5
nums = "1 2 3 4 5"
n=10
nums = "1 2 3 4 5 5 6 7 8 9"
n=5
nums = "1 4 3 2 99"
nums = list(map(int, nums.split()))
i=0
sum=0
while i < n:
    j=i+1
    if j<n:
        if nums[i]<=nums[j]:
            sum += nums[j] 
        else:
            sum += nums[i] 
    i+=1

print(sum)