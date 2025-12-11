age = int(input("Enter age: "))
base_fare = 100

if age < 5:
    fare = 0
elif age < 18:
    fare = base_fare * 0.5
elif age > 60:
    fare = base_fare * 0.7
else:
    fare = base_fare

print("₹", int(fare))
