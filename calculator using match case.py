num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))

operator = input("enter operator:")

match operator:

    case "+":
        print("sum is", num1+num2)
    case "-":
        print("subtraction is" ,num1-num2)
    case "*":
        print("multiply is ", num1*num2)
    case "/":
        print("division is ",num1/num2)
    case "%":
        print("modulo is ",num1%num2)
    case _:
        print("enter a invalid operator")
    