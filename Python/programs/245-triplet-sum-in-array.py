'''
245. Triplet Sum in Array

Given an array of N elements, find the elements A[i], A[j] and A[k] in the array such that A[i]+A[j]=A[k] and i < j < k . Print number of possibilities.

Input Description:
Input Size : 1 <= N <= 1000

Sample Input:
5
1 2 3 4 5

Sample Output:
4
'''
n=5
nums = "1 2 3 4 5"
nums = list(map(int, nums.split()))
maxnum = max(nums)
count = 0
for num in nums:
    i=1
    while i < n:
        tot = num+nums[i]
        if tot <= maxnum:
            print(num, nums[i], tot)            
        i+=1
    nums = nums[i:]