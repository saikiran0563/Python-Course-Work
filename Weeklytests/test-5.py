# #1
# import math

# circlr_geometry=lambda r:(round(math.pi*r*r,2),round(2*math.pi*r,2))

# print(circlr_geometry(7))
# print(circlr_geometry(2.5))

# #2
# import random

# def pick_random_team(members,team_size):
#     print(random.choices(members,k=team_size))

# pick_random_team(['Alice', 'Bob', 'Charlie', 'David', 'Eve'],2)
# pick_random_team(['A','B','C','D','E','F','G','H'],3)

# #3
# temp=[32,45,28,39,50,41,38]
# res=list(filter(lambda i:i>40,temp))
# print(res)

# #4
# def is_prime(n):
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return False
#     return True

# print(is_prime(11))
# print(is_prime(97))

# #5
# def reverse_number(n):
#     if n<=0:
#         return
#     print(n%10,end='')
#     return reverse_number(n//10)

# reverse_number(1234)
# reverse_number(450)

# #6
# inp=['car','cat','bat','apple']
# ch='c'
# res1=list(filter(lambda i:i.startswith(ch),inp))

# print(res1)

# #7
# from string_utils import is_palindrome,capitalize_words

# print(is_palindrome("madam"))
# print(capitalize_words("hello world"))

# #8
# words=['Apple','apple','Banana','banana','Cherry','cherry']
# res2=set(map(lambda i:i.lower(),words))

# print(list(res2))

# #9
# def countdown(n):
#     for i in range(n,-1,-1):
#         yield i

# n=int(input())
# c=countdown(n)
# for i in range(n+1):
#     print(next(c))  

#10
def nested_sum(n):
    for i in n:
        print(i)
        
