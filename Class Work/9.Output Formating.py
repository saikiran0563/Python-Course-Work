# Output Formatting and print() Examples in Python

# Understanding print() function
print("==== Basic print() demonstration ====")
print("Hello, World!")  # Simple output

# Multiple items
name = "Alice"
age = 25
score = 95.5
print("\nName:", name, "Age:", age)  # Comma-based print adds spaces by default

# Using the 'sep' argument
print("\n==== Using sep in print() ====")
print("2024", "02", "07", sep='-')

# Using the 'end' argument
print("\n==== Using end in print() ====")
print("Hello", end=", ")
print("World!")  # Continues on the same line

# Special characters
print("\n==== Special Characters ====")
print("Line 1\nLine 2")       # Line break
print("Name:\tAlice")         # Tab space

# 1️⃣ Using Commas
print("\n==== 1️⃣ Output with Commas ====")
print("Name:", name, "Age:", age, "Score:", score)
# Output: Name: Alice Age: 25 Score: 95.5

# 2️⃣ Using Modulo Operator (% Formatting)
print("\n==== 2️⃣ Output with % Formatting ====")
name = "Bob"
age = 30
score = 88.75
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))

# 3️⃣ Using f-strings (Python 3.6+)
print("\n==== 3️⃣ Output with f-strings ====")
name = "Charlie"
age = 28
score = 92.389
print(f"Name: {name} | Age: {age} | Score: {score:.2f}")

# 4️⃣ Using str.format()
print("\n==== 4️⃣ Output with str.format() ====")
name = "Diana"
age = 22
score = 89.456
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age, score))

# Summary
print("\n==== Summary ====")
print("Method  | Version | Pros                                      | Cons")
print("Commas  | All     | Simple, beginner-friendly                 | Limited formatting")
print("%       | All     | Good control over formatting              | Outdated & less readable")
print("f-str   | 3.6+    | Clean, fast, readable                     | Not in Python < 3.6")
print("format  | 2.7+,3+ | Flexible, works in Python 2 & 3           | Slightly verbose")
