'''
37. First Occurrence of Character

Problem Statement:
Given a string 'S' and a character 'K', find at what position the character 'K' occurs for the first time in 'S'.(Assume the index of string starts at 1).If the character is not found in 'S' then print -1


Input Description:
Input Size : |s| <= 100000


Sample Input:
codekata a


Sample Output:
6
'''
strings = "codekata b"
s, k = list(map(str, strings.split()))
text = tuple(s)
if k in text:
    print(text.index(k)+1)
else:
    print(-1)