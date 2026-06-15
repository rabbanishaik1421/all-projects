'''
Problem Statement:
Given a string S, print the 1st and 3rd character of the string (chracter index starts from 1).

Input Description:
Input Size : 1 <= N <= 100000

Sample Input:
codekata

Sample Output:
cd
'''
string = str(input())
newstr = [string[0], string[2]]
print("".join(newstr))