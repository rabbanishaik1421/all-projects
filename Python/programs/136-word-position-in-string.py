'''
136. Word Position in String

Problem Statement:
Given 2 strings S and X print the word position of X in S.(word count starts from 1).If the given word doesn't exists in S print '-1'.

Input Description:
The input consists of 2 strings S and X. The size of S and X are between 1 and 1000 characters (1 <= |s|, |x| <= 1000).

Output Description:
The output is the word position of X in S (starting from 1), or -1 if X is not found.

Sample Input:
codekata coding challenge
coding

Sample Output:
2
'''
text    = "codekata coding challenge"
string  = "coding"

text = list(map(str, text.split()))

if string in text:
    print(text.index(string)+1)
else:
    print(-1)