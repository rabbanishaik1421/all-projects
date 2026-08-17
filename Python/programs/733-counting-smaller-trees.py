'''
733. Counting Smaller Trees

Problem Statement:
Summer vacation, a nice time to go trekking with friends. Angel’s Landing, Utah is a best place to go for trekking but it’s also knows as the most dangerous trekking spot. Forest is a place where you can easily get lost, and this place is not exception to it. You lost trail and roam around the forest for a couple of days without food and water. After two days of search, you reach a forest area which is filled with coconut trees. It’s like a gold mine now, since the tender coconut can be a good source of food and water. You are good at climbing, but two days without food and water has made you weak. So you decide to climb only the trees of lesser height. Your task is to find out the number of trees that you would climb.

Input Description:
The first line of input will contain one integer value N - Number of coconut trees The second line of input will contain the heights of each coconut trees, each separated by spaces

Output Description:
One single number - The number of trees that you will climb

Explanation:
You will be climbing the smaller tree(s).

Sample Input:
5
1 2 3 4 5

Sample Output:
1
'''
num = int(input())
nums = list(map(int, input().split()))
min_num = min(nums)
# print(min_num)
count_num = nums.count(min_num)
print(count_num)