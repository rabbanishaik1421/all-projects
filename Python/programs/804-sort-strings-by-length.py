'''
804. Sort Strings by Length

Geekoin40
Medium
Topics
Problem Statement:
Write a Program to Sort a List According to the Length of the Elements

Input Description:
input contains String

Output Description:
print the list according to length of the string

Explanation:
print the output according to the length

Sample Input:
abcd cef e

Sample Output:
e cef abcd
'''
strs = list(map(str, input().split()))
str_freq = {}
str_new = []
for s in strs:
    str_freq[s] = len(s)

result = dict(sorted(str_freq.items(), key=lambda x:x[1]))
print(*result.keys())