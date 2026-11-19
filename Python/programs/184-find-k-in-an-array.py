'''
Problem Statement:
Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.

Input Description:
Input Size : N <= 100000

Output Description:
The output is 'yes' if the element K exists in the array, otherwise 'no'.

Sample Input:
5 2
1 2 3 4 5

Sample Output:
yes

Explanation:
HINT: Read about Binary Search
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = arr.count(k)

if count > 0:
    print("yes")
else:
    print("no")