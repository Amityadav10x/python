# positive_num

def positive_num(num):
    if num > 0 :
        return "positive number"
    return " negative number"

num = -10

print(positive_num(num))


num = 100 

if num > 0 :
    print("positive number ")
else:
    print("negative number ")

# even_odd
    
def even_odd(num):
    if num % 2 == 0:
        return "even number"
    return " odd number"
num = 11
print(even_odd(num))


num = 50

if num % 2 == 0:
    print("even number")
else:
    print("odd number")



# sum of n natural number 
    
number = 10
sum = 0

for i in range(number+1):
    sum += i
print(sum)



def natural(num):
    sum = 0
    for i in range(num+1):
        sum+=i
    return sum
    
num = 10 
print(natural(num))

# 3. in given range

number1 = 10
number2 = 20
sum = 0

for i in range(number1,number2+1):
    sum += i
print(sum)


def natural_sum(num):
    sum = 0
    for i in range(num1,num2+1):
        sum +=i
    return sum 

num1 = 10
num2 = 20

print(natural_sum(sum))

# 4. greatest of two 

num1 = 10 
num2 = 20 

if num1>num2:
    print('num1 is greatest')
else:
    print('num2 is greatest')


def greatest_two(num):
    if num1 > num2:
        return 'num1 is greatest'
    return 'num2 is greatest'

num1 = 30
num2 = 1

print(greatest_two(num))


# 5. greatest_three

num1 = 17
num2 = 19
num3 = 21

if num1 > num2 and num1>num3:
    print("num1 is greatest")
elif num2 > num1 and num2>num3:
    print("num2 is greatest")
elif num3 > num1 and num3> num2:
    print("num3 is greatest")
else:
    print("value is invalid")



def greatest_three(num):
    if num1 > num2 and num1>num3:
        return "num1 is greatest"
    elif num2 > num1 and num2 > num3:
        return 'num2 is greatest'
    elif num3 > num1 and num3>num2:
        return 'num3 is greatest'
    
num1 = 100
num2 = 200
num3 = -300

print(greatest_three(num))


# 6. leap_year

year = 2001

if (year % 4 == 0) or(year%400==0) and(year%100!=0):
    print("year is a leap year ")
else:
    print("year is not a leap year")


def leap_year(year):
    if (year % 4 == 0) or(year%400==0) and(year%100!=0):
        return 'year is a leap year'
    return 'year is not a leap year'

year = 1977

print(leap_year(year))


# 7.prime number 

def prime_num(num):
    if num < 1:
        return False
    
    for i in range(2,num):
        if num % 2 == 0:
            return False
        return True
    
num = 11

if prime_num(num):

    print(f" {num} is a prime number ")
else:
    print(f"{num} is not a prime number")
 


# 8.sum of digit of a number 
    
num = input("enter number:")
sum = 0

for i in num:
    sum = sum+int(i)
print(sum)

        
num = 1234
sum = 0
while num!=0:
    digit = int(num%10)
    sum += digit
    num = num/10
print(sum)


def sum_of_digit(num):
    sum = 0
    while num!= 0:
        digit = int(num%10)
        sum += digit
        num = num/10
    return sum
num = 12345
sum = 0
print(sum_of_digit(num))


# 9. palindrome 

def palindrome(a):
    return a == a[::-1]

print(palindrome("Amit"))
print(palindrome("radar"))



