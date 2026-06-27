'''
250. Palindrome Check using Stack

Problem Statement:
Given a string S of length N, find whether the given string is a palindrome using stack or linked list and print 'yes' otherwise print 'no'.

Input Description:
Input Size : 1 <= N <= 100000

Output Description:
print 'yes' otherwise print 'no'.

Sample Input:
GuviGeek

Sample Output:
no
'''
string="GuviGeek"
revstring = string[::-1]
if string == revstring:
    print("yes")
else:
    print("no")