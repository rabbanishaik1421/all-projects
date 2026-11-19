'''
Problem Statement:
Write a program, to find the area of a circle when the diameter is given . The input diameter is an integer and the output area should be a floating point variable with 2 point precision.

Input Description:
1

Output Description:
print the area of circle

Sample Input:
20

Sample Output:
314.00

Explanation:
314.00
'''
import math
r = 20
result = math.pi * (r ** 2)
print(f"{result:.2f}")