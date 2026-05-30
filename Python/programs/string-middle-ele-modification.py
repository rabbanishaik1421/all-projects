'''
9. String Middle Element Modification

Geekoin20
Easy
Topics
Question:
Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).


Sample Input:
hello


Sample Output:
he*lo
'''
text = "sadsad"
textlen = len(text)
textmid = textlen//2

if textlen % 2 == 1:
    text = text[:textmid]+"*"+text[textmid+1:]
else:
    text = text[:textmid-1]+"**"+text[textmid+1:]
print(text)
