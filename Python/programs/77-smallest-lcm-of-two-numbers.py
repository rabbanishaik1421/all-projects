'''
Problem Statement:
Given two numbers L,R print the smallest number which is divisible by both L and R.


Input Description:
The input consists of two numbers L and R, where 1 <= L,R <= 100000.


Output Description:
The output is the smallest number which is divisible by both L and R.


Sample Input:
10 130


Sample Output:
130
'''

import math
nums = "10 130"
a, b = list(map(int, nums.split()))
lcm = (a * b) // math.gcd(a, b)
print(lcm)
