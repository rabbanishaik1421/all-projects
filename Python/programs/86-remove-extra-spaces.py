'''
86. Remove Extra Spaces

Problem Statement:
Given a sentence S take out the extra spaces.If no extra space is present print the same as output.

Input Description:
Input Size : |s| <= 100000(complexity O(n))

Sample Input:
codekata challenge

Sample Output:
codekata challenge
'''
userInput = input()
userInput = " ".join(userInput.split())
print(userInput)