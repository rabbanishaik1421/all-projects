'''
Problem Statement:
Given a string S, print the encoded string by adding 3 to each character(a maps to d,b maps to e,c maps to f and so on).

Input Description:
Input Size : 1 <= N <= 100000

Sample Input:
RADAR

Sample Output:
UDGDU
'''
letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
letters = list(map(str, letters.split()))
text = str(input())
result = []
i=0
while i<len(text):
    letter_index = letters.index(text[i]) + 3
    if letter_index >= 26:
        letter_index = letter_index - 26
    #print(letter_index)
    result.append(letters[letter_index])
    i+=1

print("".join(result))