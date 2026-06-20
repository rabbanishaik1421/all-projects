'''
121. Binary to Decimal Conversion

Problem Statement:
Given a number N in binary format convert it to decimal number.

Input Description:
N <= 10^18

Sample Input:
101

Sample Output:
5
'''
# binval = "101"
# decval = int(binval, 2)
# print(decval)

binval = "101"
# result = 0
# for i, digit in enumerate(reversed(binval)):
#     result += int(digit) * (2 ** i)

# print(result)

result = sum([int(digit) * (2 ** i) for i, digit in enumerate(reversed(binval))])
print(result)