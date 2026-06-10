'''
85. Sort Strings by Length and Lexicographically

Problem Statement:
Given an array of N strings sort it in ascending order based on the length of the string.If two strings are found to have the same length sort them in lexicographical order.

Sample Input:
3
coding platform codekata

Sample Output:
coding codekata platform
'''
userInput = input()
arr = list(map(str, input().split()))

arr.sort(key=lambda x:(len(x), x))
print(*arr)