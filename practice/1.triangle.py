a,b,c=tuple(map(int,input().split()))
if a==b and b==c and a==c:
    print("Equ")
elif a!=b and b!=c and a!=c:
    print("Scal")
else:
    print("Iso")