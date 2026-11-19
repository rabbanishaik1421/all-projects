'''
Problem Statement:
Given a number N followed by N numbers. Find the largest number which can be formed from the given numbers and print it.
NOTE: Each number should be used exactly once.

Input Description:
Input Size : 1 <= N <= 100000

Sample Input:
5
5 6 7 8 9

Sample Output:
98765
'''
n = '5 6 7 8 9 5'
nums = list(map(int, n.split()))
unique_nums = []
for i in nums:
    if i not in unique_nums:
        unique_nums.append(i)
large_num = sorted(unique_nums, reverse=True)
print(*large_num)
