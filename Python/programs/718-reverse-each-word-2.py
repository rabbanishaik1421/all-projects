'''
718. Reverse Each Word-2

Geekoin50
Medium
Topics
Solved!
Problem Statement:
Write a program to reverse each of a sentence.
Sentence length<100 characters.

Input Description:
The single line contains a set of words separated by space and ends with a new line character.

Output Description:
Print the sentence with each word in reverse order

Explanation:
Reverse Each word of the sentence

Sample Input:
This is a sample Sentence

Sample Output:
sihT si a elpmas ecnetneS
'''
sentance = input()
revsentance = []
if(len(sentance) < 100):
    split_sentance = sentance.split(" ")
    for s in split_sentance:
        revsentance.append(s[::-1])
print(*revsentance)