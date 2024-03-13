# 1. to find largest element in the list

def largest_element(lst):
    return max(lst)

print(largest_element([10,20,30,40,50]))


# 2. to take input print sum

def add_numbers(a,b):
     return a+b
print(add_numbers(6,5))

# 3. to take 2 input and print there multiplication

def multiply_numbers(a,b):
     return a*b
print(multiply_numbers(6,6))

# 4. to check even odd 
def even_odd(n):
       if(n%2==0):
            return "even number"
       return "odd numbers"
print(even_odd(5))

# 5. calculate factorial of a number

def factorial_num(n):
     if n==0:
          return 1
     else:
          return n * factorial_num(n-1)
print(factorial_num(7))

# 6. program to take a list of numbers and return new even list
    
def return_even(lst):
     return [x for x in  lst if x%2==0 ]
print(return_even([2,4,56,78,3]))

# 7. program to take a list of numbers and return new odd numbers

def return_odd(lst):
     return [n for n in lst if n%2!=0]
print(return_odd([10,13,15,17]))


# 8. take string and reverse them

def reverse_string(s):
     return  s[::-1]
print(reverse_string("United University"))

# 9. program to sort integers in ascending order 

my_list  = [1,4,2,5,6]
my_list.sort()
print(my_list)
     
# 10. program to sort integers in descending order

my_list = [1,3,4,5,633,23,24]
sorted_list_desc = sorted(my_list, reverse=True)
print(sorted_list_desc)