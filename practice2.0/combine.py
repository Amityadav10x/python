def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))



def is_palindrome(a):
    return a == a[::-1]
print(is_palindrome("radar"))
print(is_palindrome("KaKa"))