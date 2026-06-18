'''
118. Permutation Calculation

Problem Statement:
Given 2 numbers N,K print the value of nPk(P-Permutation).

Input Description:
Input Size : K <= N <= 10

Sample Input:
5 2

Sample Output:
20
'''
import math
nums = "5 2"
n, k = list(map(int, nums.split()))

result = math.factorial(n) // math.factorial(n - k)
print(result)