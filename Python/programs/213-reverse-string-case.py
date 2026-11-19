'''
Problem Statement:
Given a string S of length N, reverse the case of each letter.

Input Description:
Input Size : N <= 100

Sample Input:
HeLlo

Sample Output:
hElLO
'''
string = str(input().strip())
result = ""
for s in string:
    if s.islower():
        result += s.upper()
    else:
        result += s.lower()
print(result)