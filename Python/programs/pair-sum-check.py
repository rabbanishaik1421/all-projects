'''
Problem Statement:
Given 2 numbers N,X and an array of N elements, check if there exists any 2 numbers in the array with sum equal to X.If found print 'yes' otherwise print 'no'


Input Description:
The input consists of two numbers N and X, and an array of N elements. N and X are up to 100000.


Output Description:
Print 'yes' if two numbers with sum equal to X are found in the array, otherwise print 'no'.


Sample Input:
4 4
2 2 0 0
'''
N, X = 4,4
nums = "1 2 0 0"
nums = list(map(int, nums.split()))
fnum = nums[0]
found = False

for i in range(N):
    j=i+1
    if j < len(nums):
        sum = fnum + nums[j]
        if(sum == X):
            found=True
            break

if found == True:
    print("yes")
else:
    print("no")
