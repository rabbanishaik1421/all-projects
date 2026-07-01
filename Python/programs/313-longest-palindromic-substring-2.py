'''
Problem Statement:
Given a string of length N, find the longest palindromic substring.

Input Description:
Input Size : 1 <= N <= 1000

Sample Input:
DIEHEIDI

Sample Output:
DIEHEID
'''
string = "HELLOWORLD"
mainstr = string[::-1]
# print(mainstr)
# print(mainstr[:1])
# print(mainstr[:1])
# print(mainstr[:2])
# print(mainstr[:3])
# print(mainstr[:4])
# print(mainstr[:5])

s = "DIEHEIDI"

longest = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if sub == sub[::-1]:
            if len(sub) > len(longest):
                longest = sub

print(longest)