# try:
#     a=int([1,2,3])
# except ZeroDivisionError:
#     print("you can not divide by zero")
# except NameError:
#     print("variable not defined")
# except TypeError:
#     print("invalid operation between different data types")
# else:
#     print("division successful")
# finally:
#     print("execution completed")

# print("program continues...")

# try:
#     b=int(input("Enter a number: "))
# except(ZeroDivisionError,NameError,TypeError,KeyError,IndexError,ValueError) as e:         
#     print("An error occurred:", e)
# else:
#     print("No error occurred, you entered:", b)
# finally:
#     print("execution completed")

# try:
#     b=int(input("Enter a number: "))
#     if b<0:
#         raise Exception("Negative value not allowed")
    
# except Exception as e:         
#     print("An error occurred:", e)
# else:
#     print("No error occurred, you entered:", b)
# finally:
#     print("execution completed")


try:
    b=int(input("Enter a number: "))
    try:
        c=int(input("Enter another number: "))
        b=c/0
    except Exception as e:
        print("An error occurred:", e)
    if b<0:
        raise Exception("Negative value not allowed")
    
except Exception as e:         
    print("An error occurred:", e)
else:
    print("No error occurred, you entered:", b)
finally:
    print("execution completed")