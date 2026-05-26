'''
Problem Statement:
Write a program to calculate the total surface area and volume of cuboid.


Input Description:
Input contains three space separated positive integers L, B, H denoting the length, width and height of cuboid respectively.


Output Description:
The output should be the total surface area and volume of the cuboid, separated by a space.


Sample Input:
1 2 3


Sample Output:
22 6
'''
userInput = "1 2 3"
l, b, h = map(int, userInput.split())
surfaceArea = 2*(l*b + b*h + l*h)
volume = l*b*h
print(surfaceArea, volume)