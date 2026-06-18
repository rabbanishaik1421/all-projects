'''
111. Bitwise AND of Array Elements

Problem Statement:
Given a number N and an array of N elements ,find the Bitwise AND of the array elements.

Input Description:
The input consists of an integer N, representing the size of the array, followed by N array elements. N <= 100000.

Output Description:
The output is the Bitwise AND of all elements in the array.

Sample Input:
4
4 3 2 1

Sample Output:
0
'''
n=4
nums = "4 3 2 1"
arr = list(map(int, nums.split()))
result = arr[0]

for i in range(1, int(n)):
    result &=arr[i]

print(result)