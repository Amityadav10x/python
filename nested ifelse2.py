num = int(input("enter number:"))


if num%15==0:
    print("it is  divisible by 15")
if num%5==0 or num%3==0:
    print("it is not divisible by 15 but divisible by 5 and 3")
else:
    print("number is not divisible by 3")

