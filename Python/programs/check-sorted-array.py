'''
102. Check Sorted Array

Problem Statement:
Given a number N, followed by an array of N elements,print 'yes' if it is a sorted array(either ascending or descending)otherwise print 'no'.

Input Description:
The input consists of a number N, followed by an array of N elements. N is between 1 and 100000.

Output Description:
The output is 'yes' if the given array is sorted (either ascending or descending), otherwise 'no'.

Sample Input:
3
2 3 7

Sample Output:
yes
'''
n = 3
arr = "2 3 7"
n = int(input())
arr = list(map(int, input().split()))

if arr == sorted(arr) or arr == sorted(arr, reverse=True):
    print('yes')
else:
    print('no')