'''
Problem Statement:
Given a string S,count the maximum number of times a character repeated in the string.If no character is repeated print '0'.


Input Description:
Input Size : 1 <= N <= 100000


Sample Input:
codekata


Sample Output:
2
'''
string = "codekata"
freq = {}
for s in string:
    freq[s] = freq.get(s, 0)+1

values = freq.values()
print(max(values))