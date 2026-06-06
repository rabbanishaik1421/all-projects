'''
Problem Statement:
Given a String S,print the number of unique characters in it.If all the characters are duplicated,then print -1.


Sample Input:
GUVIGEEK


Sample Output:
4
'''
text = str("abba")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch,0)+1

count=0
for value in freq.values():
    if value == 1:
        count+=1

print(count if count > 0 else -1)