angle = int(input("Enter angle: "))

if angle == 90:
    print("Right")
elif angle < 90:
    print("Acute")
elif 90 < angle < 180:
    print("Obtuse")
elif angle == 180:
    print("Straight")
else:
    print("Invalid Angle")
