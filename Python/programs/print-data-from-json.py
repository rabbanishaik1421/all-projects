'''
You are given a JSON string representing information about students. Each student object has the following attributes: "name", "age", and "grade". Write a function to parse the JSON string and print the name, age, and grade of each student.

Input:

A string json_str representing a JSON object containing information about students. The JSON string may contain multiple student objects.

Output:

Print the name, age, and grade of each student on separate lines.

Sample Input:

{"students": [{"name": "John", "age": 20, "grade": "A"}, {"name": "Alice", "age": 18, "grade": "B"}]}

Sample Output:

Name: John
Age: 20
Grade: A
Name: Alice
Age: 18
Grade: B
'''

data = {"students": [{"name": "John", "age": 20, "grade": "A"}, {"name": "Alice", "age": 18, "grade": "B"}]}

students = data['students']
for student in students:
    for key, value in student.items():
        print(key.capitalize(), ":", value)
