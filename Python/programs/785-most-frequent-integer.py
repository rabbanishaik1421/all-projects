'''
Problem Statement:
Print the most repeating term from the list of numbers

Input Description:
'n' spaced integers.

Output Description:
Single number 'X'

Explanation:
1 repeated the most no. of times

Sample Input:
1 2 3 4 5 6 2 2 2 1 1 1 1 1

Sample Output:
1
'''
nums = list(map(int, input().split()))
numdict = dict()
# print(numdict)
for i in nums:
    if i in numdict:
        numdict[i] += 1
    else:
        numdict[i] = 0

maxval = max(numdict.values())
for i, j in numdict.items():
    if j == maxval:
        print(i)