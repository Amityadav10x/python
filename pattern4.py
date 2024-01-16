n = int(input("enter number to print"))

for i in range(1,n+1): # loop for row
    print(" " * (n-i), end="")

    for j in range(1,2*i):
        print(j,end="")


    print()
