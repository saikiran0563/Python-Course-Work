for i in range(5):
    for space in range(i):
            print(' ',end=' ')
    for j in range(5-i):
            print(j,end=' ')
    print()


for row in range(5):
    for col in range(5):
            if row==0 or col==1 or row+col==5-1:       #row==5-1 or col==5-1 or row==5//2
                print("*",end=' ')
            else:
                print(' ',end=' ')
    print()