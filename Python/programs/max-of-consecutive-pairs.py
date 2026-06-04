'''
Problem Statement:
Given a number N followed by N elements for every 2 consecutive numbers print the maximum of the 2.


Input Description:
The input consists of an integer N, followed by N elements. N is an integer such that N <= 100000, implying an O(n) time complexity solution is expected.


Output Description:
The output is a space-separated sequence of the maximums of every two consecutive numbers from the input.


Sample Input:
5
1 1 3 0 5


Sample Output:
1 3 3 5
'''

n=5
numsarr = "1 1 3 0 5"
numsarr = "4 4 3 4 1"
arr = list(map(int, numsarr.split()))
result = []
i=0
while i<n:
    j=i+1
    if j < n:
        if arr[i] < arr[j]:
            result.append(arr[j])
        else:
            result.append(arr[i])
    i+=1

print(*result)
