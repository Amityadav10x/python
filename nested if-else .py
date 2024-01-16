num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))
num3 = int(input("enter number3:"))

if(num1>num2):
    if(num1>num3):
        print("num1 is greatest")
else:
    print("num3 is greater")
    if(num2>num1):
        if(num2>num3):
            print("num2 is greater")
    else:
        print("num1 is greater")
        
