'''
Problem Statement:
Given three numbers N,A,B. Find if it is possible to partition N into 2 equal groups containing A and B only.print 'yes' if it can be partitioned otherwise print 'no'.

Input Description:
The input consists of three numbers N, A, B. The constraints are 1<=N,A,B<=10000.

Sample Input:
20 2 3

Sample Output:
yes

Explanation:
(2,2,3,3),(2,2,3,3) ie 10+10=20=N
'''
nums = "20 2 3"
n, a, b = list(map(int, nums.split()))
# print(n, a, b)
c = a + b

