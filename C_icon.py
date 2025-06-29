print("\n")
for row in range(7):
    for col in range(7):
        if (col==1 and (row==1 or row==2 or row==3 or row==4 or row==5))or ((row==0 or row==6) and(col==2 or col==3 or col==4 or col==5 or col==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    # if col==1 or (row==0 and(col==2 or col==3 or col==4 or col==5)) or (row==4 and (col==2 or col==3 or col==4 or col==5)):
    # if (col==1 and (row==1 or row==2 or row==3))or (row==0 and(col==2 or col==3 or col==4 or col==5)) or (row==4 and (col==2 or col==3 or col==4 or col==5)):