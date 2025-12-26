from collections import Counter,defaultdict,deque

# s='python'
# s1='weakup to reality nothing ever goes as planned as you'
# l=[1,2,3,4,5,1,2,3,1,2,1,1,1,4,5,6,7,8,9,9,8,7,6]
# t=(1,2,3,4,5,1,2,3,1,2,1,1,1,4,5,6,7,8,9,9,8,7,6)
# se={1,2,3,4,5,1,2,3,1,2,1,1,1,4,5,6,7,8,9,9,8,7,6}

# print(Counter(s))
# print(Counter(s1.split()))
# print(Counter(l))
# print(Counter(t))
# print(Counter(se))

# d=defaultdict(int)
# s='python programing'
# for i in s:
#         d[i]+=1
# print(d)


# from collections import deque

# d = deque([1, 2, 3])          # creates a deque with initial elements
# print("Initial deque:", d)

# d.append(4)                  # adds element to the right end
# d.appendleft(0)              # adds element to the left end
# print("After append & appendleft:", d)

# d.pop()                       # removes element from the right end
# d.popleft()                  # removes element from the left end
# print("After pop & popleft:", d)

# d.extend([4, 5])              # adds multiple elements to the right
# d.extendleft([0, -1])         # adds multiple elements to the left
# print("After extend & extendleft:", d)

# d.rotate(1)                   # rotates deque to the right by 2 steps
# print("After rotate right:", d)

# d.rotate(-2)                  # rotates deque to the left by 2 steps
# print("After rotate left:", d)

# print("First element:", d[0]) # accesses first element
# print("Last element:", d[-1]) # accesses last element

# print("Length:", len(d))      # returns number of elements

# d.clear()                     # removes all elements from deque
# print("After clear:", d)




from itertools import combinations,permutations

s='ABC'
print(list(combinations(s,2)))
print(list(permutations(s,2)))
print(combinations(s,2))   #not a list so it will print object location
