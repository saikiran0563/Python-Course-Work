num=int(input("enter a 3-digit number:"))
a=num//100
b=(num//10)%10
c=num%10

armstrong=a**3+b**3+c**3
if armstrong==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")