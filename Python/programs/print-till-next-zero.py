'''
Print till next zero

Problem Statement:
Given a number N followed by N elements, if the number '0' occurs, print the proceeding numbers until the next '0' is encountered. If there are no balancing 0's, print -1.


Input Description:
The input consists of an integer N, followed by N elements. N is constrained such that 1 < N <= 100000.


Output Description:
Print the numbers between the first two occurrences of '0'. If there are no two '0's, print -1.


Sample Input:
10
1 1 1 0 1 0 1 1 0 1


Sample Output:
1 1 1
'''
n=10
numstr="1 1 1 0 1 0 1 1 0 1"
arr = list(map(int, numstr.split()))
first_zero = -1
second_zero = -1
for i in range(n):
    if arr[i] == 0:
        if first_zero == -1:
            first_zero = i
        else:
            second_zero = i
            break

print(arr[first_zero + 1 : second_zero])