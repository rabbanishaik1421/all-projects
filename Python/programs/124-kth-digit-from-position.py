'''
124. Kth Digit from Position

Problem Statement:
Given a number N, print the kth digit from the given position p(given order N P K).

Sample Input:
5765 2 1

Sample Output:
6
'''
nums = "5765 2 1"
nums = "5567 1 3"
nums = "5334 3 1"
n, p, k = list(map(int, nums.split()))
n=str(n)
#print(n, p, k)
i=p
count=0
k=k-1
while i < len(n):
    if count == k:
        print(n[i])
        break
    count +=1
    i+=1