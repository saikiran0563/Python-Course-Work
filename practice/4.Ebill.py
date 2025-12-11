units=int(input())
charge=0

if units<=100:
    charge=units*1
elif 100<charge<=200:
    charge=100+(units-100)*2
else:
    charge=300+(units-200)*3
print(charge)
