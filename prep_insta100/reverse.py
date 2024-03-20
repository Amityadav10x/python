num = 123456

print(str(num)[::-1])

num  = 4363327
reverse  = 0
temp = num


while num > 0:
    remainder = num % 10
    reverse = (reverse*10) + remainder
    num = num // 10

print(reverse)

