a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a + b + c == 180:
    if a == 90 or b == 90 or c == 90:
        print("Right")
    elif a < 90 and b < 90 and c < 90:
        print("Acute")
    else:
        print("Obtuse")
else:
    print("Invalid Triangle")
