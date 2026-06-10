'''
84. String Numeric Validation

Problem Statement:
Given a string S.Validate if a given string is numeric.print 'yes' if it is a numeric otherwise print 'no'.

Sample Input:
guvigeeks

Sample Output:
no
'''
userInput = input()
if userInput.isdigit():
    print('yes')
else:
    print('no')