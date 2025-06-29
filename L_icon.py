print("\n")
for row in range(7):
    for col in range(7):
        if col==0 or row==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()