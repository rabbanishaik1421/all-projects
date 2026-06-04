'''
Problem Statement:
Given 2 numbers N,K print the array after deleting the last K elements.


Input Description:
N,K <= 100000


Output Description:
The array after deleting the last K elements.


Sample Input:
5 4
1 2 3 4 5


Sample Output:
1
'''
nums = "6 4"
n, k = list(map(int, nums.split()))
numsarr = "1 2 3 4 5 6"
arr = list(map(int, numsarr.split()))

#solution 1
'''
i=0
while i<n:
    if(i<k):
        arr.pop()
    i+=1
'''

#solution 2
print(*arr[:n-k])
