marks = int(input("Enter marks: "))

if 91 <= marks <= 100:
    print(10)
elif 81 <= marks <= 90:
    print(9)
elif 71 <= marks <= 80:
    print(8)
elif 61 <= marks <= 70:
    print(7)
elif 51 <= marks <= 60:
    print(6)
elif 41 <= marks <= 50:
    print(5)
elif 0 <= marks <= 40:
    print(4)
else:
    print("Invalid Marks")
