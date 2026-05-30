'''
String Length Without Functions

Geekoin30
Easy
Topics
Problem Statement:
Given a string S, find its length(including the spaces)without using any pre-defined functions.


Sample Input:
codekata


Sample Output:
8
'''
text = "codekata"
i=0
count=0
while i<len(text):
    count +=1
    i+=1
print(count)