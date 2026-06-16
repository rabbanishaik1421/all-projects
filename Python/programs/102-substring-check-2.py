'''
103. Substring Check-2

Given 2 strings.check if the second string is a substring of the first string.Print 'yes' if there exists a valid substring otherwise print 'no'.

Input Description:
The input consists of two strings. The size of the strings (N) is between 1 and 100000 (inclusive).

Output Description:
Print 'yes' if the second string is a substring of the first string, otherwise print 'no'.

Sample Input:
codekata code

Sample Output:
yes
'''
text = "codekata ac"
str1, str2 = list(map(str, text.split()))

if str2 in str1:
    print("yes")
else:
    print("no")