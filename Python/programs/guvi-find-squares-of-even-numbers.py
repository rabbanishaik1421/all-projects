'''
find the squares of even numebrs between 383 to 403
'''
# squareslist=[]
# for n in range(150, 180):
#     if n % 3 == 0:
#         squareslist.append(n**2)

# print(squareslist)


# cubes = [n**3 for n in range(150, 180) if n % 2 != 0]
# print(cubes)
    

# def check_prime(num):
#     primes=[]
#     for n in range(1, num+1):
#         if num % n == 0:
#             primes.append(n)
        
#     return ["No" if len(primes) == 2 else "yes"]


# print(*check_prime(5))

# def check_len(string):
#     if len(string)>=5 and len(string)<=9:
#         return True
#     else:
#         return False
    
# strings = ['apple', 'mango', 'grap', 'banana']
# result = list(filter(check_len, strings))
# print(result)

# person = [
#     {"name" : "Raghava", "age" :28},
#     {"name" : "Css" , "age" :32},
#     {"name" : "John", "age" :29},
#     {"name" :"Sandeep" , "age" :28},
#     {"name" : "Chandan", "age" :45}
# ]

# persons = list(filter(lambda person:person["age"]>30, person))
# print(persons)

squares = [n**2 for n in range(4, 46) if n % 2 == 0]
print(squares)

#Can you make an iterator to give next iterator
