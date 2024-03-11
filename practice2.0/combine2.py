# To check palindrome 

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("radar"))

print(is_palindrome("amit"))


# to check factorial number 

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# to check maximum number 

def largest(lst):
    return max(lst)
print(largest([32,34,33,55,1000]))

# to check minimum number

def smallest(lwt):
    return min(lwt)
print(smallest([32,45,33,66,77,450]))