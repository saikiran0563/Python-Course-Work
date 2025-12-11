day = input("Enter day: ")
age = int(input("Enter age: "))

# Check if weekend
if day.lower() in ["saturday", "sunday"]:
    base_price = 200
else:
    base_price = 150

# Apply child discount
if age < 12:
    price = base_price * 0.5
else:
    price = base_price

print("₹", int(price))
