'''
Problem Statement:
Given a number N and K followed by N elements and K elements. Now insert the given K elements one by one into the array and print the maximum in the array after each insertion .


Input Description:
Input Size : K <= N <= 10000(read about priority queues and implement)


Sample Input:
5 2
1 2 3 4 5
5 4


Sample Output:
5 5
'''
nums = "5 2"
n, k = list(map(int, nums.split()))

nums1 = "1 2 3 4 5"
arr1 = list(map(int, nums1.split()))
maxnum = max(arr1)

nums2 = "5 4"
arr2 = list(map(int, nums2.split()))

for num in arr2:
    if num > maxnum:
        maxnum=num

print(maxnum)