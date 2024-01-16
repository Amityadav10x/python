num = int(input("enter number:"))
for i in range(1, num+1): #loop for rows
    for j in range(1, i+1):#loop for columns
        print(j, end="")
    print()
