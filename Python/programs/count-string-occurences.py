'''
Problem Statement:
Given a sentence and string S, find how many times S occurs in the given sentence.If S is not found in the sentence print -1


Input Description:
Input Size : |sentence| <= 1000000(complexity O(n)).


Output Description:
The output is the number of times S occurs in the given sentence, or -1 if S is not found.


Sample Input:
I enjoy doing codekata
codekata


Sample Output:
1
'''
text = "I enjoy doing codekata codekata"
s = "codekata"
textlist = list(map(str, text.split()))
count=0
for str in textlist:
    if str == s:
        count+=1

if count == 0:
    print(-1)
else:
    print(count)