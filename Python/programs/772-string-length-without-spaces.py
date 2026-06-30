'''
Problem Statement:
Let "A" be a string. Remove all the whitespaces and find it's length.
Input Description:
A string is provide as an input

Output Description:
Remove all the whitespaces and then print the length of the remaining string.

Sample Input:
Lorem Ipsum

Sample Output:
10

Explanation:
Lorem Ipsum becomes LoremIpsum after removing the whitespaces and hence the length of this string is equal to 10.
'''
string = str(input())
string = string.replace(" ", "")
print(len(string))