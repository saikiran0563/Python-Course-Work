amount = int(input("Enter amount: "))

# Available denominations
notes = [2000, 500, 100, 50, 20, 10]

print("Denominations:")

for note in notes:
    count = amount // note
    if count > 0:
        print(f"{count} x {note}")
    amount = amount % note
