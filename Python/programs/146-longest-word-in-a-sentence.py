'''
Problem Statement:
Find the word having maximum length in a given sentence and print it. If two words are of same length return the first occuring word of max-length.

Input Description:
The input consists of a sentence where its size |s| is less than or equal to 100000.

Output Description:
The output is the word with the maximum length.

Sample Input:
guvi geek

Sample Output:
guvi
'''
inputstr = list(map(str, input().split()))
freq = {}
for s in inputstr:
    freq[s] = len(s)
    
minlen = (max(freq.values()))
res = None
for k, v in freq.items():
    if v == minlen:
        res = k
        break
    
print(res)