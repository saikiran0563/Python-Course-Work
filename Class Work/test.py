# def order(v, i):
#     #recursion
#     if i >len(v):
#         return
#     print(v*i)
#     order(v, i+1)
# order("abcd", 1)



# def length(s):
#     cnt=0
#     for i in s:
#         cnt+=1
#     return cnt

# s="python programming"
# print("length:",length(s))


# l=list(map(int,input().split()))
# double=list(map(lambda i:i+i,1))
# print(double)

# n=int(input("entrer the nth term: "))
# a,b,c=0,1,0
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
# print(c)


# a = "Hello, World!"
# b = a.split(" ")
# print(b)


# def sample_generator():
#     yield 1
#     yield 2
#     yield 3
# gen = sample_generator()
# print(next(gen))

# a="hello"
# b="world"
# print(a+b)
# print(a,b)
# import math

# print(math.ceil(5.3))

# try:
#     balance = 3000
#     withdraw = int(input("Enter amount: "))
#     if withdraw > balance:
#         raise Exception("Insufficient balance")
#     balance -= withdraw
#     print("Transaction successful")
# except Exception as e:
#     print("Error:", e)
