num1 = 1
num2 = 6
sum = 0

for i in range(num1,num2+1):
    sum +=i
    print(sum)




def recursum(sum,a,b):
    if a > b:
        return sum
    return a + recursum(sum,a+1,b)

a = 10
b = 20
sum = 0

print(recursum(sum,a,b))
