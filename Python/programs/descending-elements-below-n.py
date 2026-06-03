'''
Problem Statement:
Given a number N and an array of N elements, print all elements lesser than N in descending order. If no element found print -1.


Input Description:
The input consists of a number N, and an array of N elements. N is between 1 and 10000 (inclusive).


Output Description:
Print all elements from the array that are lesser than N, in descending order. If no such elements are found, print -1.


Sample Input:
5
2 14 15 14 3


Sample Output:
3 2
'''
#Example 1
#N=5
#nums = "2 14 15 14 3"

#Example 2
N=4
nums = "5 6 7 8"

arr = list(map(int, nums.split()))
arr = sorted(arr)

descarr = []
found = False
i=0
while i < len(arr):
    if arr[i] < N:
        descarr.append(arr[i])
        found = True
    i+=1

if found == True:
    print(*descarr[::-1])
else:
    print(-1)
