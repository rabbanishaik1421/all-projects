'''
282. Rotated Sorted Array Count

Problem Statement:
Find the count k by which array has been rotated in the rotated sorted array. Given a number N followed 2 arrays A and B of length N. Find the amount K by which the array has been rotated.

Input Description:
The input consists of a number N, followed by two arrays A and B of length N. N is at most 100000.

Output Description:
The output should be the integer K, representing the count by which the array has been rotated.

Sample Input:
4
4 3 2 5
3 2 5 4

Sample Output:
1
'''
n = 4
arr = "4 3 2 5"
rarr = "3 2 5 4"

n=5
arr = "5 3 6 1 0"
rarr = "6 1 0 5 3"

arr = list(map(int, arr.split()))
rarr = list(map(int, rarr.split()))

i=0
count=0
while i < int(n):
    rotatedarr = arr[i:]+arr[:i]
    if list(rarr) == list(rotatedarr):
       break
    else:
        count+=1
    i+=1

print(count)