num = [10,12,13,31,154,133]
num1 = ['A','b','c','d','e']
num.append(5)
print(num)

num.pop(5)
print(num)

num.extend(num1)
print(num)

def list1 (n):
    if n%2 == 0:
        return " even number "
    return " odd number "
print(list1(50))
