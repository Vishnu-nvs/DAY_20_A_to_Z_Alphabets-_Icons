print("\n")
for row in range(7):
    for col in range(7):
        if col==0 or col==6 or ((row==col and col <= 3) or (row + col == 6 and col >= 3)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()