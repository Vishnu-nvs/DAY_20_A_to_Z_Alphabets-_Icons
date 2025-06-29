print("\n")
for row in range(7):
    for col in range(9):
        if  (row==col and row<5) or (row+col==8 and row<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()