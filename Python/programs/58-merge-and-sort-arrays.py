'''
Problem Statement:
Given 2 array of size N and M.merge them in sorted order and print it.


Input Description:
The input consists of two integers N and M representing the sizes of the arrays, followed by N integers for the first array and M integers for the second array. The constraints are |N||M| <= 100000.


Output Description:
The output is the merged sorted array.


Sample Input:
5 4
1 2 3 4 5
1 2 3 4


Sample Output:
1 1 2 2 3 3 4 4 5
'''
num = "5 4"
n, k = list(map(int, num.split()))
nums1 = "1 2 3 4 5"
nums2 = "1 2 3 4"
arr1 = list(map(int, nums1.split()))
arr2 = list(map(int, nums2.split()))

arr = arr1 + arr2
print(sorted(arr))
