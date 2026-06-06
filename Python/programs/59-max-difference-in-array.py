'''
Problem Statement:
Given an array, find the maximum difference between any two elements.


Input Description:
Input Size : N <= 1000000(complexity O(n) or O(nlogn))


Sample Input:
5
1 2 3 4 5


Sample Output:
4
'''
n=5+1
num="1 1 1 1 1"
arr = list(map(int, num.split()))
count=0
result = []
for i in range(n):
    for j in range(i+1, n):
        if(j<n-1):
            result.append(arr[j]-arr[i])

result = max(result)
if result == 0:
    print(-1)
else:
    print(result)