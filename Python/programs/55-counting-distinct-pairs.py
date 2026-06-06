'''
Problem Statement:
Given an array A of N elements, count the number of distinct pairs (i,j) such that i < j and A[i] < A[j].If no such pairs can be made print -1


Input Description:
The input consists of an integer N, representing the number of elements, followed by N space-separated integers representing the elements of array A.


Output Description:
The output is a single integer representing the count of distinct pairs (i,j) such that i < j and A[i] < A[j]. If no such pairs can be made, print -1.


Sample Input:
5
1 2 3 4 5


Sample Output:
10
'''
n=5
i=0
count=0
nums = "1 2 3 4 5"
arr = list(map(int, nums.split()))

pairs = set()
for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            pairs.add((arr[i], arr[j]))

if len(pairs) == 0:
    print(-1)
else:
    print(len(pairs))