'''
Problem Statement:
Given an array, find the maximum difference between any two elements.


Input Description:
Input Size : N <= 1000000(complexity O(n) or O(nlogn))


Sample Input:
5
1 2 3 4 5


Sample Output:
4
'''
n=5+1
num="1 2 3 4 5"
nums = list(map(int, num.split()))
diff = max(nums) - min(nums)
print(diff)