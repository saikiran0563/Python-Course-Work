products = [
    ("Rice", 60), ("Wheat Flour", 45), ("Sugar", 40), ("Milk", 25),
    ("Eggs (12 pcs)", 70), ("Cooking Oil", 130), ("Tea Powder", 90),
    ("Salt", 20), ("Bread", 30), ("Soap", 25)
]

print("\n-------- Grocery Store --------\n")
print(f"{'Index':<8}{'Product':<20}{'Price':<10}")
print("-" * 40)

for i, (n, p) in enumerate(products, 1):
    print(f"{i:<8}{n:<20}{p:<10}")

print("\nEnter index and quantity (example: 1 2 5 3 10 1)")
data = input("Input: ").split()

# Convert to integers safely
numbers = []
for d in data:
    if d.isdigit():
        numbers.append(int(d))
    else:
        print(f"Skipping invalid item: {d}")

# Ensure even count
if len(numbers) % 2 != 0:
    print("\n⚠ WARNING: Last number has no quantity. Ignoring last number.")
    numbers = numbers[:-1]

cart = []

for i in range(0, len(numbers), 2):
    idx = numbers[i]
    qty = numbers[i+1]

    if 1 <= idx <= len(products):
        cart.append((idx, qty))
    else:
        print(f"\n⚠ Invalid product index: {idx} (ignored)")

print("\n-------------- FINAL BILL --------------")
total = 0

print(f"{'Product':<20}{'Qty':<5}{'Total'}")
print("-" * 35)

for idx, qty in cart:
    name, price = products[idx - 1]
    item_total = price * qty
    total += item_total
    print(f"{name:<20}{qty:<5}{item_total}")

gst = total * 0.05

print("-" * 35)
print(f"Sub Total: Rs.{total}")
print(f"GST (5%): Rs.{gst:.2f}")
print(f"Grand Total: Rs.{total + gst:.2f}")
print("----------------------------------------")
