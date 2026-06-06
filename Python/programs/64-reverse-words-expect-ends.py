'''
Problem Statement:
Given a string S consisting of a sentence, the task is to reverse every word of the sentence except the first and last character of the words.


Input Description:
The input consists of a string S representing a sentence.


Output Description:
The output is the modified string with every word reversed except its first and last characters.


Sample Input:
guvi coding platform


Sample Output:
gvui cnidog proftalm.
'''
text = "guvi coding platform"
strings = list(map(str, text.split(" ")))

arr = []
for string in strings:
    if len(string)>3:
        i=1    
        result = ""
        fstr=string[0]
        estr=string[len(string)-1]
        while i<len(string)-1:
            result+=string[i]
            i+=1
            
        result = result[::-1]
        result = fstr+result+estr
        arr.append(result)
    else:
        arr.append(string)

print(*arr)