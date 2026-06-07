'''
Problem Statement:
Given a string S, print the reverse of the string after removing the vowels.If the resulting string is empty print '-1'.


Input Description:
Input Size : 1 <= N <= 100000


Sample Input:
codekata


Sample Output:
tkdc
'''
vowels = ['a', 'e', 'i', 'o', 'u']
string = "codekata"
for v in vowels:
    if string.find(v):
        string = string.replace(v, "")

revstr = string[::-1]
print(revstr)