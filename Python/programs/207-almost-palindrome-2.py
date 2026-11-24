'''
207. Almost Palindrome-2

Problem Statement:
Given a string S, check if it can be made into a palindrome by making atmost one character replacement,if it results in palindrome print 'yes' otherwise print 'no'

Sample Input:
abb

Sample Output:
yes
'''
string = input()

i = 0
j = len(string) - 1
count = 0

while i < j:
    if string[i] != string[j]:
        count += 1
    i += 1
    j -= 1

if count <= 1:
    print("yes")
else:
    print("no")