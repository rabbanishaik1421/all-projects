'''
41. Common Characters in Strings

Problem Statement:
Given 2 strings,check whether they have any common characters.If found print 'yes' else print 'no'.

Input Description:
Input Size : |s| <= 100000(O(n))

Sample Input:
guvi guvigeeks

Sample Output:
yes
'''
s="HHH"
found=False
text="guvigeeks"
for ch in s:
    if ch in text:
        found=True
        break

if found == True:
    print("yes")
else:
    print("no")
    