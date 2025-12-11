ch = input("Enter a character: ")

ascii_value = ord(ch)   

if 65 <= ascii_value <= 90:
    print("Uppercase Letter")
elif 97 <= ascii_value <= 122:
    print("Lowercase Letter")
elif 48 <= ascii_value <= 57:
    print("Digit")
else:
    print("Special Symbol")
