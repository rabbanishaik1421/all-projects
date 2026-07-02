'''
Problem Statement:
Write a code to get an integer N and print values from 1 till N in a separate line.

Input Description:
A single line contains an integer N.

Output Description:
Print the values from 1 to N in a separate line.

Sample Input:
5

Sample Output:
1
2
3
4
5

Explanation:
The values from 1 upto N is printed.
'''
n = int(input())
for i in range(1, n+1):
    print(i)