'''
Problem Statement:
Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).


Input Description:
Input Size : |s| <= 10000000(complexity O(n))


Sample Input:
codekata


Sample Output:
ocedakat
'''
s = "codekata"
result = []

for i in range(0, len(s) - 1, 2):
    result.append(s[i + 1])
    result.append(s[i])

if len(s) % 2 == 1:
    result.append(s[-1])

print("".join(result))    
