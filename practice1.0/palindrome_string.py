num = input("enter text  to check the palindrome string:")

rev  = num[::-1]

if(rev==num):
    print("text is palindrome")
else:
    print("text is not palindrome")