print("\n")
for row in range(6):
    for col in range(9):
        if row + col==4 or (row==3 and (col==5 or col==3 or col==4)) or (col-row==4 and row<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()