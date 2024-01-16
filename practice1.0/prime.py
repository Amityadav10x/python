num = int(input("enter number to check prime number: "))


if(num<=1):
    print("it is not a prime number")

else:

    for i in range(2,num): 

        if num % i ==0: 
         print("this is not a prime number ")
         break

    else:
       print("number is a prime number ")

