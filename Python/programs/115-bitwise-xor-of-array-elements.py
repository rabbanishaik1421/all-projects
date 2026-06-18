'''
115. Bitwise XOR of Array Elements

Problem Statement:
Given a number N and an array of N elements, find the Bitwise XOR of the array elements.

Input Description:
The input consists of an integer N, representing the size of the array, followed by N array elements. The input size N is at most 100000.

Output Description:
The output is the Bitwise XOR of all elements in the array.

Sample Input:
2
2 4

Sample Output:
6
'''
n=5
nums = "1 7 6 5 2"
arr = list(map(int, nums.split()))

result = arr[0]

for i in range(1, n):
    result ^=arr[i]

print(result)

