'''
Problem Statement:
Given base(B) and height(H) of a triangle find its area.

Input Description:
The input consists of the base (B) and height (H) of a triangle. The input size N is up to 1000000.

Sample Input:
2 4

Sample Output:
4
'''
b, h = map(int, input().split())
area = (b * h) / 2

if area.is_integer():
    print(int(area))
else:
    print(area)