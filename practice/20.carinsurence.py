num = input("Enter a 4-digit number: ")

if int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]):
    print("Lucky")
else:
    print("Not Lucky")
