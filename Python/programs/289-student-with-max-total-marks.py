'''
289. Student with Max Total Marks

Problem Statement:
Given an arraylist A of string type which has name#mark1#mark2#mark3 format. Retrieve the name of the student who has scored max marks(total of three).

Input Description:
The input consists of an arraylist A of string type, where each string is in 'name#mark1#mark2#mark3' format. The size of A is at most 100000.

Output Description:
The output is the name of the student who has scored the maximum total marks.

Sample Input:
arun#12#12#12
deepak#13#12#12

Sample Output:
deepak

Explanation:
For the given input, 'arun' has a total score of 12+12+12=36, and 'deepak' has a total score of 13+12+12=37. Since Deepak has the maximum total score, 'deepak' is the output.
'''
student1 = "arun#12#12#12"
student2 = "deepak#13#12#12"

#student1 = input()
#student2 = input()
marks = {}

studentmarks1 = student1.split("#")
studentmarks2 = student2.split("#")
marks1 = int(studentmarks1[1])+int(studentmarks1[2])+int(studentmarks1[3])
marks2 = int(studentmarks2[1])+int(studentmarks2[2])+int(studentmarks2[3])
if marks1 < marks2:
    print(studentmarks2[0])
else:
    print(studentmarks1[0])