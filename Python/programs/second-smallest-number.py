'''
33. Second Smallest Element

Geekoin40
Medium
Topics
Problem Statement:
Given a number N followed by N elements, find the second smallest element.If it cannot be found then print -1


Input Description:
Input Size : N <= 100000 (ie do it in O(log n) time complexity)


Sample Input:
5
1 2 3 4 5


Sample Output:
2
'''
nums = "1 2 3 4 5"
arr = list(map(int, nums.split()))

smallest = float('inf')
second_smallest = float('inf')

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num

if second_smallest == float('inf'):
    print(-1)
else:
    print(second_smallest)