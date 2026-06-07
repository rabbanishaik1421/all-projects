'''
Problem Statement:
Given a day, print 'yes' if it is a holiday otherwise print'no'.Assume that weekend days are holidays


Sample Input:
saturday
monday


Sample Output:
yes
no
'''
weekends = ["sunday", "saturday"]
weekend = "saturday"
weekend = weekend.lower()
if weekend in weekends:
    print('yes')
else:
    print("no")
