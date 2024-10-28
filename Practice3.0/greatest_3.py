num1 = 10
num2 = 20
num3 = -10

if num1 > num2 and num1 > num3:
    print("num1 is greatest")
elif num2 > num1 and num2 > num3:
    print("num2 is greatest")
else:
    print("num3 is greatest")


def find_greatest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return " num1 is greatest"
    elif num2 > num1 and num2> num3:
        return " num2 is greatest"
    else:
        return " num3 is greatest"

num1 = 10
num2 = 20
num3 = 30

print(find_greatest(num1,num2,num3))
   
