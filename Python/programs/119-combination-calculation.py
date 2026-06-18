'''
119. Combination Calculation
Problem Statement:
Given 2 numbers N,K print the value of nCk(C-Combination).

Input Description:
Input Size : K <= N <= 10

Sample Input:
5 2

Sample Output:
10
'''
#formula
#nCk=n! // k!(n−k)!
import math
nums = "5 2"
n, k = list(map(int, nums.split()))

result = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

print(result)