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
