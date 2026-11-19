'''
Problem Statement:
Given a string S, retain the character(s) once irrespective of number of times it occurs in the given string.

Input Description:
Input Size : |S| <= 100000

Sample Input:
aabbaa

Sample Output:
ab
'''
string = str(input().strip())
result = ""
for s in string:
    if s not in result:
        result += s
print(result)