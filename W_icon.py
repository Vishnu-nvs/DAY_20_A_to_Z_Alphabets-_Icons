print("\n")
for row in range(7):
    for col in range(7):
        if col==0 or col==6 or(row==col and row>2) or (row+col==6 and row>2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()