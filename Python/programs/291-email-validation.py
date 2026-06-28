'''
Problem Statement:
Email Validation: Given a string S, check if it is a valid email id based on the following Conditions. 
1)@ should be present; 
2)@ & . should not be repeated; 
3)there should be atleast four characters between @ and .; 4)there should be at-least 3 characters before @; 5)the end of mail id should be .com; If its a valid email id print 'yes' else print 'no'.

Input Description:
The input consists of a single string S. The length of S is at most 100000 characters.

Output Description:
The output is 'yes' if the given string S is a valid email ID according to the specified conditions, and 'no' otherwise.

Sample Input:
test@gmail.com

Sample Output:
yes
'''


email = "ts@gmail.com"

if email.count('@') != 1:
    print("no")
else:
    at = email.index('@')
    #Condition 2:
    if email.count(".") != 1 :
        print("no")
    
    else:        
        dot = email.rfind(".")

        if dot < at:
            print("no")
        
        elif dot - at - 1 < 4:
            print("no")
        
        elif at<3:
            print("no")

        elif not email.endswith(".com"):
            print("no")
        else:
            print("yes")
