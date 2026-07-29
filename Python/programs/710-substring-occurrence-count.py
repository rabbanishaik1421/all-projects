'''
710. Substring Occurrence Count

Problem Statement:
Count the occurrence of substring

Find the occurrence of a sub string in a parent string

Input Description:
Input contains the string and the sub string

Output Description:
print the count

Sample Input:
hgjghjhab
ab

Sample Output:
1

Explanation:
1
'''
strings = "hgjghjhab"
substr = "ab"
print(strings.count(substr))