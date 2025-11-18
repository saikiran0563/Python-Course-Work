# Input Formatting Examples in Python

# 1. String Input
name = input("Enter your full name: ")
print("Name:", name)
# Example: Ankit Sharma

# 2. Integer Input
quantity = int(input("\nEnter the number of items: "))
print("Quantity:", quantity)
# Example: 5

# 3. Float Input
price = float(input("\nEnter the product price: "))
print("Price:", price)
# Example: 299.99

# 4. Input as List (Space-separated)
names = input("\nEnter employee names (space-separated): ").split()
print("Names list:", names)
# Example: Ankit Ravi Sneha => ['Ankit', 'Ravi', 'Sneha']

# 5. Input as List (Comma-separated)
tags = input("\nEnter tags (comma-separated): ").split(',')
print("Tags:", tags)
# Example: sale,discount,new => ['sale', 'discount', 'new']

# 6. List of Integers
marks = list(map(int, input("\nEnter marks (space-separated integers): ").split()))
print("Marks:", marks)
# Example: 89 76 94 82 => [89, 76, 94, 82]

# 7. List of Floats
weights = list(map(float, input("\nEnter weights (space-separated floats): ").split()))
print("Weights:", weights)
# Example: 55.6 62.1 70.3 => [55.6, 62.1, 70.3]

# 8. Tuple Input
dimensions = tuple(map(int, input("\nEnter length, width, height: ").split()))
print("Dimensions (tuple):", dimensions)
# Example: 10 20 15 => (10, 20, 15)

# 9. Set Input (removes duplicates)
selected_ids = set(map(int, input("\nEnter selected image IDs: ").split()))
print("Selected IDs (set):", selected_ids)
# Example: 101 102 103 101 104 => {101, 102, 103, 104}

# 10. Dictionary Input using eval()
# Note: Only use eval() when input is trusted.
profile = eval(input("\nEnter user profile as a dictionary: "))
print("Profile:", profile)
# Example: {'name': 'Ravi', 'age': 30, 'role': 'admin'}

# 11. Multiple Inputs with Unpacking
username, password = input("\nEnter username and password (space-separated): ").split()
print("Username:", username)
print("Password:", password)
# Example: user01 mypassword123

print("\n--- Summary of Input Types Demonstrated Successfully ---")
