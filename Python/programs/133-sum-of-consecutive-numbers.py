'''
133. Sum of Consecutive Pairs

Problem Statement:
Given a number N and an array of N elements, find the sum of the sums obtained by considering all consecutive pairs of adjacent elements.

Input Description:
The input consists of a number N and an array of N elements. N <= 100000.

Output Description:
The output is the sum of the sums obtained by considering all consecutive pairs of adjacent elements.

Sample Input:
5
1 2 3 4 5
'''
n=5
nums = "1 2 3 4 5"
nums = "1 4 3 2 99"
arr = list(map(int, nums.split()))
narr = []
i=0
total=0
while i<=n:
    j=i+1
    if j<n:
        narr.append([arr[i],arr[j]])
    i+=1

for l in narr:
    total += sum(l)    

print(total)