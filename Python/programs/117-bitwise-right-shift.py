'''
117. Bitwise Right Shift

Problem Statement:
Given 2 numbers N and K print the number after performing bitwise right shift 'K' times(upto 2 decimal places).

Input Description:
The input consists of two numbers, N and K, where 1 <= N, K <= 1000.

Output Description:
The output is the number N after performing a bitwise right shift K times, rounded to 2 decimal places.

Sample Input:
5 2

Sample Output:
1
'''
n, k = list(map(int, input().split()))
print(n >> k)