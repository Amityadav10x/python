num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))
num3 = int(input("enter number3:"))

if(num1>num2):
    print("num1 is greater")
elif(num2>num3):
    print("num2 is greater")
elif(num3>num1 and num2):
    print("num3 is greater")
else:
    print("no is greater")