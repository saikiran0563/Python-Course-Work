m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

average = (m1 + m2 + m3) / 3

if average > 90 and m1 > 70 and m2 > 70 and m3 > 70:
    print("Admitted")
elif average > 80:
    print("Waitlisted")
else:
    print("Rejected")
