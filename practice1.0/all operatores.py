

# Arithmetic operators
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulo = num1 % num2
exponentiation = num1 ** num2

print("\nArithmetic Operators:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulo: {num1} % {num2} = {modulo}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")

# Comparison operators
print("\nComparison Operators:")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")

# Logical operators
bool1 = True
bool2 = False

print("\nLogical Operators:")
print(f"{bool1} and {bool2}: {bool1 and bool2}")
print(f"{bool1} or {bool2}: {bool1 or bool2}")
print(f"not {bool1}: {not bool1}")

# Assignment operators
a = 5
b = 2

print("\nAssignment Operators:")
a += b
print(f"a += b: {a}")
a -= b
print(f"a -= b: {a}")
a *= b
print(f"a *= b: {a}")
a /= b
print(f"a /= b: {a}")
a %= b
print(f"a %= b: {a}")
a **= b
print(f"a **= b: {a}")
