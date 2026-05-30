'''
Problem Statement:
Given 2 numbers N and K followed by N elements, find the Kth smallest element. If the element cannot be found then print -1


Input Description:
The input consists of two numbers N and K, followed by N elements. N <= 100000.


Output Description:
The output is the Kth smallest element. If the element cannot be found, print -1.


Sample Input:
5 2
1 1 2 4 5


Sample Output:
2

'''
nums = "5 2"
numslist = "1 1 2 4 5"
n, k = list(map(int, nums.split()))
arr = set(map(int, numslist.split()))
arr = sorted(arr)
print(arr[k-1])