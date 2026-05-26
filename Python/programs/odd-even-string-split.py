'''Problem Statement:
Given a string S, print 2 strings such that first string containing all characters in odd position(s) and other containing all characters in even position(s).


Sample Input:
XCODE


Sample Output:
XOE CD

'''
text= "xcode"
evenstr=""
oddstr=""
i=0
strlen = len(text)
while i<strlen:
    if(i % 2 == 0):
        evenstr += text[i]
    else:
        oddstr += text[i]
    i=i+1

print(evenstr)
print(oddstr)


