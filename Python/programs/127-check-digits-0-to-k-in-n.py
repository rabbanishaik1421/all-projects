'''
127. Check Digits 0 to K in N

Problem Statement:
Given a number N and a number K, check if it has all digits from 0 to k in it.

Input Description:
Input Size : N <= 100000

Sample Input:
1234034 4

Sample Output:
yes
'''
nums = "1234034 4"
num, k = list(map(int, nums.split()))
found = True
for n in range(0, k+1):
    if str(n) not in str(num):
        found = False

print("yes" if found else "no")