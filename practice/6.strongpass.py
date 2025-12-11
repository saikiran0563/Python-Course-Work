password = input("Enter a password: ")

if len(password) >= 8:

    if any(ch.isupper() for ch in password):

        if any(ch.isdigit() for ch in password):

            special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
            if any(ch in special_chars for ch in password):
                print("Strong Password")
            else:
                print("Weak Password (No special character)")
        else:
            print("Weak Password (No digit)")
    else:
        print("Weak Password (No uppercase letter)")
else:
    print("Weak Password (Less than 8 characters)")
