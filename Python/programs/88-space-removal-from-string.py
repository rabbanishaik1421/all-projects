'''
Problem Statement:
Given a string/sentence remove all the spaces and print the result.

Input Description:
Input Size : |s| <= 1000000(complexity O(n))

Sample Input:
guvi geeks

Sample Output:
guvigeeks
'''
string = "guvi geeks"
strs = list(map(str, string.split()))
print("".join(strs))
