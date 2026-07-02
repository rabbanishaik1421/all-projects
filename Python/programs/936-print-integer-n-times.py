'''
Problem Statement:
Write a code to get 2 integers A and N. Print the integer A, N times in separate line.

Input Description:
First line contains an integer A.
Second line contains an Integer N.

Output Description:
Print the integer A, N times in a separate line.

Explanation:
The integer A(2) is printed N(3) times.

Sample Input:
2 3

Sample Output:
2
2
2
'''
n, k = list(map(int, input().split()))
for i in range(1, k+1):
    print(n)