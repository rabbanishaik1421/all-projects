'''
Problem Statement:
Given a string/sentence print its corresponding camelcase convention.


Input Description:
Input Size : |s| <= 1000000(complexity O(n))


Sample Input:
guvi geeks


Sample Output:
GuviGeeks
'''
strings = "guvi geeks"
s=list(map(str, strings.split(" ")))
result = ""
for string in s:
    result += string.title()

print(result)