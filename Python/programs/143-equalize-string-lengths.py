'''
143. Equalize String Lengths

Problem Statement:
Given 2 strings S1 and S2,work on the strings such that both string has the same number of characters.To adjust the length reduce number of exceeding characters from longer string.

Sample Input:
guvi
geeks

Sample Output:
guvigeek
'''
str1, str2 = list(map(str, input().split()))
len1 = len(str1)
len2 = len(str2)

minlen = len1
if len1 > len2:
    minlen = len2
    
newstr = str1[:minlen]+str2[:minlen]
print(newstr)