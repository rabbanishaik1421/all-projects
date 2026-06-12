'''
Problem Statement:
Given a string S change upper case to lowercase and lowercase to uppercase.

Input Description:
The input consists of a string S with size |s| <= 10000000 (complexity O(n)).

Sample Input:
CodEkaTa

Sample Output:
cODeKAtA
'''
text = "CodEkaTa"
newtext=[]
for ch in text:
    if ch.isupper() == True:
        newtext.append(ch.lower())
    else:
        newtext.append(ch.upper())
    
print("".join(newtext))