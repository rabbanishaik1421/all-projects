'''
129. Binary to Hexadecimal Conversion

Problem Statement:
Given a binary number convert it to hexadecimal.

Sample Input:
1100100

Sample Output:
64
'''
num = 1100100
binary = str(num)
hexaval = hex(int(binary, 2))[2:]
print(hexaval.upper())