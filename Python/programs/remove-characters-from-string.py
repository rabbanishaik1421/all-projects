'''
Problem Statement:
Given a string two strings S1 and S2, remove characters from the S1 which are present in the S2.If S1 becomes empty then print -1


Input Description:
Input Size : N <= 100000


Sample Input:
GUVI GEEK


Sample Output:
UVI
'''
text = "GUVI GEEK"
s1, s2 = list(map(str, text.split())) 

i=0
while i<len(s2):
    if s2[i] in s1:
        s1 = s1.replace(s2[i], '', 1)
    i+=1

print(s1)