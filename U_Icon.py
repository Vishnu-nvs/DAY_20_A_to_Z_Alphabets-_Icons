print("\n")
for row in range(7):
    for col in range(8):
        if ((col==0 or col==7) and (row==0 or row==1 or row==2 or row==3 or row==4)) or (row==6 and (col==2 or col==3 or col==4 or col==5)) or (row==5 and(col==1 or col==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()