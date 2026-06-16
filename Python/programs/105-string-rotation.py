'''
105. String Rotation

Problem Statement:
Given a string S and an integer K, print the string obtained by rotating the orignal string by K positions.

Input Description:
Input Size : 1 <= N, K <= 100000

Sample Input:
katacode 4

Sample Output:
codekata
'''
text = "codekata 4"
text = "geekguvi 4"
text = "Hunter 2"
str, n = list(map(str, text.split()))
n = int(n)
revstr = str[n:len(str)]+str[0:n]
print(revstr)