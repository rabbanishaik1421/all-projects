'''
753. Diagonal Sum of a Matrix

Problem Statement:
The first input is row_count(<10), the second input is column_count(<10), third the array elements are given

Input Description:
three inputs where the first input is the size of number of elements in row, second input is the size of number of elements in column and the third set is to get the matrix input

Output Description:
sum of all the elements in the diagonal

Sample Input:
3 3
1 2 3
4 5 6
7 8 9

Sample Output:
25

Explanation:
(1+5+9+7+3) = 25
'''
rows, cols = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(rows)]

total = 0

for i in range(rows):
    total += matrix[i][i]
    total += matrix[i][cols - 1 - i]

if rows % 2 == 1:
    total -= matrix[rows // 2][cols // 2]

print(total)