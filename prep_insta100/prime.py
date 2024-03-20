num = 10
flag = 0

for i in range(2,num):
    if num % i == 0 :
        flag = 1
        break
if flag == 1:
        print("prime")
else:
    print("not prime")




def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = 10
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not a prime number")

