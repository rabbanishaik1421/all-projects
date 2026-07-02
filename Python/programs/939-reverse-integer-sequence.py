'''
Problem Statement:
Write a code to get an integer N and print the values from N to 1.

Input Description:
A single line contains an integer N.

Output Description:
Print the values from N to 1 in a separate line.

Explanation:
The values from N upto 1 is printed.

Sample Input:
10

Sample Output:
10
9
8
7
6
5
4
3
2
1
'''
n = int(input())
for i in range(n, 0, -1):
    print(i)