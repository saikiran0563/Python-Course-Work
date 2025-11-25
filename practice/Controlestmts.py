a,b,c=tuple(map(int,input().split()))
if a==b and b==c and a==c:
    print("Equ")
elif a!=b and b!=c and a!=c:
    print("Scal")
else:
    print("Iso")

ch=input()
vol='aeiouAEIOU'

if ch in vol:
    print("vol")
elif ch.isalpha():
    print("con")
elif ch.isdigit():
    print("digit")
else:
    print("special")


units=int(input())
charge=0

if units<=100:
    charge=units*1
elif 100<charge<=200:
    charge=100+(units-100)*2
else:
    charge=300+(units-200)*3
print(charge)

