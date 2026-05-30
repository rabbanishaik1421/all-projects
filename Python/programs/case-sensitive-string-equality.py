'''
36. Case-Sensitive String Equality

Geekoin40
Medium
Topics
Problem Statement:
Given 2 strings S1 and s2, check whether they are case senitively equal without using any predefined function(case sensitive).If they are not same print 'no'


Sample Input:
guvi guvi


Sample Output:
yes
'''
strings = "guvi guvi"
s1, s2 = list(map(str, strings.split()))
slen1 = len(s1)
slen2 = len(s2)
same = True
if slen1 == slen2:
    #print(slen1, slen2)
    i=0
    while i<slen1:
        if s1[:i] != s2[:i]:
            same=False
        i+=1
else:
    same=False

if same == True:
    print('yes')
else: 
    print('no')
