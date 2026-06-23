'''
386. String Value Calculator

Problem Statement:
Value of 'a' is 1, Value of 'b' is -2, Value of 'c' is 3, Value of 'd' is -4 and so on.

The value of a string for example , "fry" is calculated as:

value("fry") = value('f') + value('r') + value('y') = -6 + -18 + 25 = 1

Given N strings, find the value of each string.

Input Description:
The first line consists N, the number of strings S.
Then N lines follow, each containing a string.

Output Description:
Print N lines, denoting the value of the string.

Sample Input:
2
fry
a

Sample Output:
1
1
'''
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=2
string = "fry"

total = 0
for s in string:
    position = alphabets.index(s) + 1
    if position % 2 == 0:
        position = -position
    
    total += position

print(total)