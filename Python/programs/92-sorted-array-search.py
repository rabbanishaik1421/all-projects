'''
Problem Statement:
Given 2 numbers N,K followed by a sorted array of N elements, search and tell if an element K is present in the array.print 'yes' if element is present otherwise print 'no'.

Input Description:
Input Size : 1 <= N <= 1000000000000000(Do it in logN time complexity)

Output Description:
print 'yes' if element is present otherwise print 'no'.

Sample Input:
3 2
2 3 7

Sample Output:
Yes
'''
n,k = list(map(int, input().split()))
nums = list(map(int, input().split()))
i=0
found=False
while i<n:
    if nums[i] == k:
        found=True
    i+=1

print('yes' if found==True else 'no')