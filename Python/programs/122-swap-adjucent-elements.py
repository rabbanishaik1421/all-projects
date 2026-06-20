'''
122. Swap Adjacent Elements

Problem Statement:
Given an array of N elements switch(swap) the element with the adjacent element and print the output.

Sample Input:
5
3 2 1 2 3

Sample Output:
2 3 2 1 3
'''
n=5
nums = "3 2 1 2 3"
nums = list(map(str, nums.split()))
pos=0
i=2
swapnums=[]
for num in range(n-2):
    #print(nums[4:6])
    newnum = nums[pos:i]
    for j in reversed(newnum):
        swapnums.append(j)
    pos += 2
    i += 2

print(*swapnums)