# -----------------------------
# Python List Operations Demo
# Version: Python 3.11.4
# -----------------------------

# 1. List Creation
print("\n--- List Creation ---")
l = []
l = list()
l = [1, 2, 3, 4, 5, 6]
print("List l:", l)

# 2. Nested Lists and Indexing
print("\n--- Nested Lists and Indexing ---")
l = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", l)
print("First element:", l[0])
print("Second element of first list:", l[0][1])
print("First element of third list:", l[2][0])

# 3. List Operations
print("\n--- List Operations ---")
print("[1,2,3] + [4,5,6] =", [1,2,3] + [4,5,6])
print("[1,2]*5 =", [1,2]*5)

# 4. Membership
print("\n--- Membership ---")
l = [1,1,1,1,1,1,2]
print("List:", l)
print("2 in l?", 2 in l)
print("6 in l?", 6 in l)

# 5. Slicing
print("\n--- Slicing ---")
names = ['ajay','krishna','shekar','santhosh','harsha','varun','shiva']
print("names[1:3] =", names[1:3])
print("names[-1:-4:-1] =", names[-1:-4:-1])
print("names[::2] =", names[::2])
print("names[::-1] =", names[::-1])

# 6. Modification
print("\n--- Modification ---")
l = [10, 20, 30, 40, 50]
print("Original list:", l)
print("Memory ID before:", id(l))
l[1] = 20.3
l[2] = 30 + 4j
l[3] = "string"
print("Modified list:", l)
print("Memory ID after:", id(l))

# 7. Adding Elements
print("\n--- Adding Elements ---")
l.append([1,2,3])
l.append((10,202,30))
l.extend([70,80,100,90,20,10])
l.insert(0, 999)
print("After appending and inserting:", l)

# 8. Removing Elements
print("\n--- Removing Elements ---")
l.remove(999)
l.pop(2)
del l[0]
print("After remove, pop, del:", l)
l.clear()
print("After clear:", l)

# 9. Index, Count, Sort, Reverse
print("\n--- Index, Count, Sort, Reverse ---")
l = [10,20,30,40,50,60,70,80]
print("List:", l)
print("Index of 30:", l.index(30))
print("Count of 10:", l.count(10))
l.append(10)
l.sort()
print("Sorted list:", l)
l.sort(reverse=True)
print("Sorted descending:", l)
l.reverse()
print("Reversed:", l)

# 10. Copying Lists
print("\n--- Copying Lists ---")
a = [1,2,3,4,5]
b = a
b.append(6)
print("a =", a)
print("b =", b)
c = a.copy()
c.append(9)
print("c =", c)
print("a (unchanged) =", a)

# 11. Built-in Functions
print("\n--- Built-in Functions ---")
l = [1, 2, 3, 3, 4, 4, 8, 8]
print("max(l):", max(l))
print("min(l):", min(l))
print("len(l):", len(l))

# 12. any() and all()
print("\n--- any() and all() ---")
l = [0, 0.0, '', [], (), {}, set(), False]
print("any(l):", any(l))   # False (all empty or false)
print("all(l):", all(l))   # False
l.append(1)
print("After appending 1:", l)
print("any(l):", any(l))   # True (since 1 is True)
print("all(l):", all(l))   # False (since others are False)

a = [1,2,3,4,5,6]
print("all(a):", all(a))   # True (all True values)

print("\n--- End of Program ---")
