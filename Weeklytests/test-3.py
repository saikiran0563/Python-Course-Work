# sal = int(input("Enter the salary: "))
# tax = 0

# if sal <= 250000:
#     tax = 0
# elif 250000 < sal <= 500000:
#     tax = sal * 0.05
# elif 500000 < sal <= 1000000:
#     tax = sal * 0.2
# elif sal > 1000000:
#     tax = sal * 0.3


# print(f'Tax amount: {tax}\nSalary after tax: {sal - tax}')

# n = int(input("No. of persons: "))
# amount = 0
# for i in range(n):
#     age = int(input())
#     if age < 5:
#         amount +=0
#     elif 5 <= age < 18:
#         amount += 100
#     elif 18 <= age < 60:
#         amount += 150
#     else:
#         amount += 120
# print(amount)


# hrs=int(input("enter the hours:"))
# fee=0
# if hrs<=2:
#     fee=30
# elif 2<hrs<24:
#     fee=30+(hrs-2)*10
# elif hrs==24:
#     fee=200

# print(fee)


# name=input("Enter the name:")
# qua=int(input("enter the quantity: "))



# n=int(input("Enter the size of n: "))
# for i in range(n):
#     for j in range(n):
#         print((i+j)%2,end=' ')
#     print()



# bill={1:1500,2:1300,3:5000}
# ch=int(input("Enter the choice: "))
# n=int(input("Enter number of people: "))

# print(bill[ch]*n)



amount=float(input("Enter the amount: "))
discount=0
if 0<=amount<1000:
    discount=0
elif 1000<=amount<5000:
    discount=amount*0.05
elif 5000<=amount<10000:
    discount=amount*0.1
elif amount>=10000:
    discount=amount*0.15

print(amount-discount)


str_pin=1234
for i in range(3):
    pin=int(input("enter the pin:"))
    if pin==str+pin:
        print("access granted")
        break
else:
    print("ATM Blocked.Try again later")


