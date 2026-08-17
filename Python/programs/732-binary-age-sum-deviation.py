'''
732. Binary Age Sum Deviation

Problem Statement:
Kanishkar a computer geek, is invited to address a group of school kids on children's day. He was asked to write a program to find the sum of the ages of the kids in the class. But he did a small mistake. He wrote a program to find the sum of the binary equivalent(considered as integer) of all the ages of the students. Find the magnitude of deviation from the actual desired output.

Input Description:
First line of input will contain one single integer N corresponding to the number of students
Second line of input will contain the age of the students, each age separated with a space

Output Description:
One number - the deviation from the desired result and the actual output

Sample Input:
2
5 6

Sample Output:
200

Explanation:
Binary equivalent of 5 - 101
Binary equivalent of 6 - 110
sum - 211
sum of 5 and 6 - 11
Deviation - 200
'''
n = input()
child_ages = list(map(int, input().split()))
child_ages_sum = sum(child_ages)
# print(child_ages_sum)
bin_age_sum=0
for age in child_ages:
    bin_age = bin(age)[2:]
    bin_age_sum += int(bin_age)
# print(bin_age_sum)
deviation = bin_age_sum - child_ages_sum
print(deviation)