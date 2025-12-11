balance = int(input("Enter your account balance: "))
withdraw = int(input("Enter amount to withdraw: "))

if withdraw >= 500:

    if withdraw % 100 == 0:

        if withdraw <= balance:
            print("Success")
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Amount (Not a multiple of 100)")
else:
    print("Invalid Amount (Minimum withdrawal is 500)")
