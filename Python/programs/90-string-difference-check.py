'''
90. String Difference Check

Geekoin50
Medium
Topics
Problem Statement:
Given 2 strings and a number K, check whether they differ exactly by K characters.

Input Description:
Input Size : |s| <= 100000(complexity O(nlogn) or O(n))

Sample Input:
codekata codeguvi 4

Sample Output:
yes
'''
strings = "codekata codeguvi 4"
str1, str2, n = list(map(str, strings.split()))
#str1, str2, n = list(map(str, input().split()))
i=0
count=0
while i<len(str1):
    if str1[i] != str2[i]:
        count+=1
    i+=1

print('yes' if int(n)==count else 'no')
