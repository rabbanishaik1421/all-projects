'''
Problem Statement:
Given a number N and 2 arrays A and B of sorted order of size N, print the common elements.If it is not found print -1.


Input Description:
Input Size : 1 <= N <= 100000


Sample Input:
5
1 1 1 1 1
1 2 3 4 5


Sample Output:
1
'''
n=5
nums1 = "1 2 4 8 10" 
nums2 = "1 4 8 18 20"

arr1 = list(map(int, nums1.split()))
arr2 = list(map(int, nums2.split()))

arr3 = set()
for i in arr1:
    for j in arr2:
        if i == j:
            arr3.add(i)

print(sorted(arr3))