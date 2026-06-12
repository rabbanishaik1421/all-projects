'''
Problem Statement:
Given numbers A,B find A^B.

Input Description:
Input Size : 1 <= A <= 5 <= B <= 50

Sample Input:
3 4

Sample Output:
81
'''
n, k = list(map(int, input().split()))
result = n ** k 
print(result)