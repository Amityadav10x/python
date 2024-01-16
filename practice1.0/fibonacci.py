a = 0
b = 1

print(a)
print(b)

n = int(input("enter number to check fibonacci series :"))

if n == 1:
    print(1)
else:

    for i in range (2,11):
        c = a+b
        a = b
        b = c
        print(c)