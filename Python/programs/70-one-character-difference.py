'''
Problem Statement:
Given 2 strings check whether they differ exacly by one character.If yes then print 'yes' otherwise print 'no'


Input Description:
Input Size : |s| <= 100000(complexity O(nlogn) or O(n))


Sample Input:
codekata codekate


Sample Output:
yes
'''
strings = "codekata codekate"
str1, str2 = list(map(str, strings.split()))

count=0
i=0
while i<len(str1):
    print(str1[i], str2[i])
    if str1[i] == str2[i]:
        result=""
    else:
        count+=1
    
    i+=1

print("yes" if count == 1 else "no")