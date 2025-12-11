num = int(input("Enter a 4-digit number: "))

a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10

if (a + b) == (c + d):
    print("Lucky")
else:
    print("Not Lucky")
