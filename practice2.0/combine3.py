# Reverse the list

def reverse_list(lst):
    lst.reverse()
my_list = [2,3,4,6,6,7,4]
reverse_list(my_list)
print(my_list)


# sort the list 

def sort_list(st):
    st.sort()
my_list = [23,43,55,66,33,23]
sort_list (my_list)
print(my_list)

# delete duplicates

def delete_duplicates(dlt):
    return list(set(dlt))
print(delete_duplicates([10,12,10,13]))

# factorial number 

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# largest number 

def largest(lst):
    return max(lst)

print(largest([10,12,13,141,191,180]))

# sortest number 

def sortest(stt):
    return min(stt)

print(sortest([10,20,33,50,22]))

# palindrome 

def palindrome(s):
   return  s == s[::-1]
print(palindrome("radar"))
print(palindrome("amit"))