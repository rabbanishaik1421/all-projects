'''
116. Bitwise Left Shift

Problem Statement:
Given 2 numbers N,K print the number after performing bitwise left shift 'K' times.

Input Description:
The input consists of two integers, N and K, where 1 <= N, K <= 1000.

Output Description:
The output is the integer N after performing a bitwise left shift K times.

Sample Input:
5 2

Sample Output:
20
'''
nums = "5 2"
n, k = list(map(int, nums.split()))
print(n << k)