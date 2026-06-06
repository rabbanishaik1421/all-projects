'''
Problem Statement:
Given an array of N elements,find the maximum length of increasing continuous sub-array.If it is not found print '-1'.


Input Description:
Input Size : N <= 100000


Output Description:
The maximum length of the increasing continuous sub-array, or '-1' if not found.


Sample Input:
5
1 2 3 2 1


Sample Output:
3
'''
n = 5
num = "1 2 3 2 1"
arr = list(map(int, num.split()))

for i in range(n):
    j=i+1
    if j<n:
        print(arr[i], arr[j])
