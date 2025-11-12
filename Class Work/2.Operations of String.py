'''
Operations on String
--------------------
Python String Operations Practice
Version: Python 3.11.4 or above
'''

# ------------------------------
# String Initialization
# ------------------------------
name = "sai"
name1 = "kiran"
print("name + name1:", name + name1)   # Output: saikiran

# Empty strings
s = ''
s = ""
s = ''' '''
s = "' '"

# ------------------------------
# Concatenation
# ------------------------------
name = 'Ajay'
name1 = "Krishna"
print(name + name1)             # Output: AjayKrishna
print(name + ' ' + name1)       # Output: Ajay Krishna

# ------------------------------
# Repetition
# ------------------------------
print(name * 10)                # Repeats 'Ajay' 10 times
print('*' * 100)                # Prints 100 stars
print('-' * 10)                 # Prints 10 hyphens

# ------------------------------
# Indexing
# ------------------------------
name = 'Ajay Kumar'
print(name[3])      # y
print(name[-2])     # a
print(name[-5])     # K
print(name[1])      # j

# ------------------------------
# Slicing
# ------------------------------
names = 'AjayKrishnaSatishNishithaPreethiRuchitha'
print(names[0:4])     # Ajay
print(names[4:11])    # Krishna
print(names[11:17])   # Satish
print(names[17:25])   # Nishitha
print(names[25:32])   # Preethi
print(names[32:])     # Ruchitha
print(names[::-1])    # Reverse the string

# ------------------------------
# Reverse Parts Individually
# ------------------------------
print(names[10:3:-1])   # anhsirK
print(names[16:10:-1])  # hsitaS
print(names[24:16:-1])  # ahtihsiN
print(names[31:24:-1])  # ihteerP
print(names[39:31:-1])  # ahtihcuR

# ------------------------------
# Membership Operators
# ------------------------------
print('Ajay' in names)           # True
print('nithin' in names)         # False
print('sahithi' not in names)    # True

# ------------------------------
# Case Transformations
# ------------------------------
print(names.upper())    # All uppercase
print(names.lower())    # All lowercase
print(names.swapcase()) # Swap upper/lower

# ------------------------------
# Capitalization and Title
# ------------------------------
l = 'python programming language'
print(l.capitalize())   # Python programming language
print(l.title())        # Python Programming Language

# ------------------------------
# Casefold (for aggressive lowercasing)
# ------------------------------
print("ß".casefold())   # ss

# ------------------------------
# Alignment and Centering
# ------------------------------
print(l.center(50, '*'))
print(l.center(50, '-'))
print(l.center(50, '_'))
print(l.ljust(50, '-') + ':')  # Left align
print(l.rjust(50, '-'))        # Right align

# ------------------------------
# Zero Fill
# ------------------------------
print('2'.zfill(6))       # 000002
print('202'.zfill(6))     # 000202
print('202123'.zfill(6))  # 202123

# ------------------------------
# Searching and Counting
# ------------------------------
print(names.find('j'))     # 1
print(names.find('a'))     # 2
print(names.find('Ajay'))  # 0
print(names.rfind('a'))    # 39
print(names.index('K'))    # 4
print(names.count('a'))    # 5
print(names.count('e'))    # 2
print(names.count('i'))    # 6

# ------------------------------
# Replace Examples
# ------------------------------
print(names.replace('a', '*'))
print(names.replace('sh', ''))
print(names.replace('sh', '00'))
print(names.replace('sh', '-00-'))
print(names.replace('Ajay', 'Anirudh'))

# ------------------------------
# Translation Example (maketrans + translate)
# ------------------------------
trans_table = str.maketrans('AEIOUaeiou', '1234500000')
print(names.translate(trans_table))   # Replaces vowels with digits

print("\n--- End of String Operations Program ---")
