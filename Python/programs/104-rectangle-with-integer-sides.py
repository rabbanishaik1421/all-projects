'''
104. Rectangle with Integer Sides

Problem Statement:
Given 2 numbers P and A which are the perimeter and area of a rectangle respectively, find if there can actually be a rectangle with this perimeter and area having integer sides.If there exists such rectangle print 'yes' otherwise print 'no'.

Input Description:
Input Size : 1 <= P,A <= 100000

Output Description:
The output is 'yes' if such a rectangle exists, otherwise 'no'.

Sample Input:
20 25

Sample Output:
yes
'''
nums = "20 25"
p, a = list(map(int, nums.split()))

#area = l * w
#permiter = 2 * (l+w)

found=False
for l in range(1, a+1):
    if a % l == 0:
        w = a // l

        if 2 * (l+w) == p:
            found=True
            break

print("yes" if found else "no")