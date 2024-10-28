num = 7

if num % 2 == 0:
    print("number is even")
else:
    print("Given number is odd")




num = int(input("Enter number to check number output:"))

if num%2==0:
    print("number is even")
else:
    print("number is odd")




def even_odd(number):
    if number % 2 ==0:
        return "even"
    else:
        return "odd"
    
num = int(input("Enter number :"))
result = even_odd(num)
print(f"The number {num} is {result}")


