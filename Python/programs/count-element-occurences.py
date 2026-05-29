'''
Problem Statement:
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.


Sample Input:
6 2
1 2 3 5 7 8


Sample Output:
1
'''
N=6
K=2
i=0
nums = "1 2 3 5 7 8"
arr = list(map(int, nums.split()))
count=0
while i<N:
    if K == arr[i]:
        count += 1
    i +=1
else:
    print("Done")
print(count)