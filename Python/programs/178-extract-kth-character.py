'''
Problem Statement:
Given a string and a number K.Print every kth character from the beginning.

Sample Input:
string 3

Sample Output:
r g
'''
text = "string"
n = 3
i=1
result = []
for s in text:
    if i % n == 0:
        result.append(s)
    i+=1
print(*result)