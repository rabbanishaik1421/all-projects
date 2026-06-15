'''
Problem Statement:
Given a number N and an array of N elements, find the maximum of the elements (using Bitwise AND) and print the output.


Input Description:
Input Size N <= 100000


Sample Input:
4
2 4 4 2


Sample Output:
4
'''
n=int(input())
nums = list(map(int, input().split()))

i=0
maxn=int(0)
while i < n:
    num = int(nums[i])
    #print(num)
    if maxn < num:
        maxn=num
    i+=1
    
print(maxn)