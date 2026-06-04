'''
Problem Statement:
Given an value 'M' follwed by array of M elements in which the elements would have been rotated for certain 'N' times from the intial array representation where all elements are arranged in ascending order.Print the 'N' or print -1 if there is no rotation made or cannot be determined.Note: 1<=N<=length of the given array.

Sample Input:
5
15 18 2 3 6 12

Sample Output:
2
'''
n=5
nums = "15 18 2 3 6 12"
numsarr = list(map(int, nums.split()))

count = 0
for k in range(len(numsarr)):
    rotated = numsarr[k:] + numsarr[:k]
    if(rotated == sorted(rotated)):
        count = k
        break

if count == 0:
    print(-1)
else:
    print(count)