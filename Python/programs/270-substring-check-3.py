'''
Problem Statement:
Given 2 strings S1 and S2. Find if String2 is substring of String1. If it is print the index of the first occurrence. else print -1.

Input Description:
Input Size : 1<= N <= 100000

Output Description:
If it is print the index of the first occurrence. else print -1.

Sample Input:
test123string
123

Sample Output:
4
'''
str1 = input()
str2 = input()

index = -1

for i in range(len(str1) - len(str2) + 1):
    if str1[i:i + len(str2)] == str2:
        index = i
        break

print(index)