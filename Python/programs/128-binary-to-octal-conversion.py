'''
Problem Statement:
Given a binary number convert it into octal format.

Sample Input:
1100100

Sample Output:
144
'''
binary = "10100"
octval = oct(int(binary, 2))[2:]
print(octval)