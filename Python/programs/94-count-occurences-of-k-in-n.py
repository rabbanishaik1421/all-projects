'''
Problem Statement:
Given 2 numbers N and K.Print the number of occurrences of K in N.If K is not found print '-1'.

Input Description:
1 <= N <= 100000, 0 <= K <= 9

Sample Input:
1000 0

Sample Output:
3
'''
nums = "1000 0"
n, k = list(map(str, nums.split()))
print(n)
i=0
count=0
while i<len(str(n)):
    if n[i] == k:
        count+=1
    i+=1

print(count if count>0 else -1)