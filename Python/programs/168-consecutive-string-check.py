'''
168. Consecutive String Check

Problem Statement:
Given a number N and an array of N strings, find if two consecutive words are same.

Input Description:
The input consists of a number N, representing the size of the array, followed by N strings. N is an integer such that N <= 1000.

Output Description:
The output is 'yes' if two consecutive words in the array are the same, otherwise 'no'.

Sample Input:
5
code
overload
vishal
sundar
anish

Sample Output:
no
'''
num = int(input())
string1 = list()
for i in range(num):
    string1.append(input())

freq = {}
i = 0
while i< num:
    freq[string1[i]] = freq.get(string1[i], 0)+1
    i += 1
    
found = "no"
for k, v in freq.items():
    if v > 1:
        found = "yes"

print(found)
