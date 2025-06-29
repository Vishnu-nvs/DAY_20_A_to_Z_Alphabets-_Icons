print("\n")
for row in range(7):
    for col in range(7):
        if  (row+col==6 and row<3) or (row==col and row<4) or (col==3 and(row==4 or row==5 or row==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()