'''
Problem Statement:
Given a string 'S' and a character 'K', find how many times 'K' got repeated in 'S'.If 'K' is not found in 'S' print -1


Input Description:
The input consists of a string 'S' and a character 'K'. The size of string 'S' is at most 100000.


Output Description:
The output is the count of character 'K' in string 'S'. If 'K' is not found, print -1.


Sample Input:
codekata a


Sample Output:
2
'''
strings = "codekata a"
s, k = list(map(str, strings.split()))
s = tuple(s)
i=0
count=0
while i<len(s):
    if s[i] == k:
        count+=1
    i+=1
print(count)