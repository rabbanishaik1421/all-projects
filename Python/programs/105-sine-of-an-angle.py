'''
106. Sine of an Angle

Problem Statement:
Given an angle A, print the sine of the given angle.

Sample Input:
30

Sample Output:
0.5
'''
import math

#angle = int(input())
angle = 30
result = round(math.sin(math.radians(angle)), 10)

if result.is_integer():
    print(int(result))
else:
    print(result)