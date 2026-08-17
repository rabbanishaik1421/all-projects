'''
Problem Statement:
Input consists of positive numbers of mxn matrix where the value of m rows and n column is to be obtained during runtime. Size of row<10 and column<10

Input Description:
First input is row size, second input is column size and the third input is the elements of the matrix

Output Description:
product of the elements of along the diagonal of the input matrix

Explanation:
95173 = 945

Sample Input:
3 3
1 2 3
4 5 6
7 8 9

Sample Output:
945
'''
rows, cols = list(map(int, input().split()))
# print(rows, cols)
matrix = [list(map(int, input().split())) for _ in range(rows)]
# print(matrix)

product = 1
for i in range(rows):
    product *= matrix[i][i]
    if i != cols - 1 - i:
        product *= matrix[i][cols - 1 -i]
    
    
print(product)