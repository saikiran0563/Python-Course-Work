# Creating empty tuples
t = ()
print(t)   # ()

t = tuple()
print(t)   # ()

# Creating tuple with values
t = (1, 2, 3, 4, 5, 1, 2, 4)
print(t)

# WRONG method – tuple() accepts only ONE argument
# t = tuple(1,2,3,4)   # ❌ TypeError

# Correct method – pass ONE iterable (list/tuple)
t = tuple((1, 2, 3, 4, 5))
print(t)

# Tuple without parentheses
t = 1, 2, 3, 4, 5
print(t)

# Single element tuple
t = (1)      # ❌ Not tuple → integer
print(t)

t = (1,)     # ✔ Tuple with one element
print(t)

# Tuple of datatypes
t = ('int','float','complex','bool','set','dict','list','tuple','string')
print(t)

# Indexing
print(t[1])    # float
print(t[-1])   # string
print(t[-2])   # tuple
print(t[-5])   # set
print(t[2])    # complex
print(t[3])    # bool

# Slicing
print(t[3:6])       # ('bool', 'set', 'dict')
print(t[-1:-4])     # ()
print(t[-1:-4:-1])  # ('string','tuple','list')
print(t[-3:])       # ('list','tuple','string')
print(t[2::-1])     # ('complex','float','int')
print(t[::2])       # ('int','complex','set','list','string')
print(t[::-2])      # ('string','list','set','complex','int')

# Tuple concatenation
t1 = (1, 2, 3)
t2 = (7, 8, 9)
print(t1 + t2)

# Tuple repetition
print(t1 * 5)

# Membership operators
print(3 in t1)
print(5 in t1)
print(4 not in t1)
print(1 not in t1)

# Tuple unpacking
t = (10, 20, 30)
a, b, c = t
print(a, b, c)

# Unpacking user details
t = ('Uname', 'mail@gmail.com', 'Pwd@123')
uname, mail, pwd = t
print(uname, mail, pwd)

# Tuple methods
t = (1, 2, 3, 1, 2, 3, 1, 2)
print(t.count(2))   # 3
print(t.count(3))   # 2
print(t.count(1))   # 3

print(t.index(2))   # 1
# print(t.index(5)) # ❌ Error: 5 not found

# Built-in functions
print(len(t))   # 8
print(max(t))   # 3
print(min(t))   # 1
print(sum(t))   # 15

# Tuple is immutable
# t[1] = 14   # ❌ TypeError: tuple does not support item assignment
