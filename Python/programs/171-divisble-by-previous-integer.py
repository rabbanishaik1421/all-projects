'''
Problem Statement:
Given a number N and an array of N integers, print all integers which are divisible by the previous integer.

Input Description:
The input consists of an integer N, followed by an array of N integers. N is at most 100000.

Output Description:
The output consists of all integers from the array that are divisible by their preceding integer.

Sample Input:
5
1 2 3 6 7

Sample Output:
2 6
'''
n = int(input())
nums = list(map(int, input().split()))
i=0
count=0
result=[]
while i<len(nums):
    j=i+1
    
    if j < n:
        if nums[j] % nums[i] == 0:
            result.append(nums[j])
    i+=1

print(*result)
