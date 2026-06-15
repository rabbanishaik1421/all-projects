'''
96. Least Repeated Characters

Problem Statement:
Given a string, print the least repeated characters in the string.If there are more than one character repeated preserve the order as in the input.

Input Description:
Input Size : 1 <= N <= 100000

Sample Input:
codeKata challenge

Sample Output:
odKthng
'''
#strings = "codeKata challenge"
str1 = input()
newstr = str1
newstr = newstr.replace(" ", "")
freq={}
for ch in newstr:
    freq[ch]=freq.get(ch, 0)+1

minval = min(freq.values())
uniquestr = []
for k, v in freq.items():
    if v == minval:
        uniquestr.append(k)

print("".join(uniquestr))