'''
100. Power of Two Check-2

Problem Statement:
Given a number N, check if it is a power of 2.

Input Description:
The input consists of a number N, where 1 <= N <= 100000.

Output Description:
Print 'yes' if N is a power of 2, otherwise print 'no'.

Sample Input:
64

Sample Output:
yes
'''
num = 16
p=1
while p<num:
    p *=2

if p == num:
    print('yes')
else:
    print("no")