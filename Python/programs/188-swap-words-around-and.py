'''
Problem Statement:
Given a sentence interchange the between the word 'and'.


Input Description:
The input consists of a single string S, representing the sentence, with a maximum length of 1,000,000 characters.


Sample Input:
jack and jill went up and down to get water


Sample Output:
jill and jack went down and up to get water
'''
# Solution 1
string = "jack and jill went up and down to get water"
split_string    = string.split(" ")
newstring       = string.split(" ")

i=0
for s in split_string:
    if s == "and":
        # print(s)
        # print(i)
        newstring[i-1] = split_string[i+1]
        newstring[i+1] = split_string[i-1]    
    i+=1

print(*newstring)

# Solution 2:
string = input()

arr = string.split()

for i in range(len(arr)):
    if arr[i] == "and" and i > 0 and i < len(arr)-1:
        arr[i-1], arr[i+1] = arr[i+1], arr[i-1]

print(*arr)