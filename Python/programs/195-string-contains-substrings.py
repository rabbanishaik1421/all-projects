'''
195. String Contains Substrings

Problem Statement:
Given a string S, print 'yes' if the strings 'GUVI' and 'GEEK' is present case-sensitively in the string else print 'no'.

Input Description:
The input consists of a string S. The size of the string S is between 1 and 100 characters (inclusive).

Output Description:
Print 'yes' if both 'GUVI' and 'GEEK' are present case-sensitively in the string S, otherwise print 'no'.

Sample Input:
Vishal_Sundar prepared this question

Sample Output:
no
'''
str1 = "GUVI"
str2 = "GEEK"
string = str(input())

if str1 in string and str2 in string:
    print("yes")
else:
    print("no")