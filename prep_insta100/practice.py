def greatest_of_two(num1,num2):
    if num1 > num2:
        return "num1 is bigger then num2"
    return "num2 is bigger then num1"

num1 = 100
num2 = 20
print(greatest_of_two(num1,num2))


def less_of_two(num1, num2):
    if num1 < num2 :
        return "num1 is lesser than num2"
    return "num2 is lesser than num1"

num1 = 10
num2 = 30
print(less_of_two(num1,num2))


def is_prime(num):
    if num <= 1:
        return False
    for i in range (2,num):
        if num%i==0:
            return False
        return True
    
num = 10

if is_prime(num):
        print(f"{num} is prime" )
else:
        print(f"{num} is not prime ")

    

def palindrome(s):
     return s == s[::-1]

print(palindrome("Amit"))
print(palindrome("RADAR"))

if palindrome is True:
     print("yes this is palindrome")
else:
     print("no this not a palindrome")


def leap_year(year):
     if (year%4==0) or (year%400 == 0) and (year%100!=0):
          return 'leap year'
     return 'not a leap year'

year = 10001

print(leap_year(year))


def positive_number(num):
     if num > 0:
          return 'number is positive number '
     elif num == 0:
          return 'number is equal to zero'
     elif num < 0:
          return 'number is negative'
     else:
          return 'invalid number'
     
num = 0
print(positive_number(num))

num = 12345
print(str(num)[::-1])


cost_prise= 100
seller_prise = 130

if cost_prise > seller_prise:
     profit  = seller_prise-cost_prise
     print("seller is in the profit")
elif cost_prise > seller_prise:
     loss = seller_prise< cost_prise
     print("seller is in the loss")
elif cost_prise == seller_prise:
     print("seller is no in the loss as well profit")

else:
     print("seller is kamchalu")



