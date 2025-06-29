print("\n")
for row in range(7):
    for col in range(8):
        if row==0 or col==4 or (row==6 and(col==1 or col==2 or col==3) or (row==5 and col==1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()