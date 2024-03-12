# extract even numbers 

def extract_even(lst):
    return [x for x in lst if x%2==0]
print(extract_even([10,11,12,11,13]))

# extract_odd numbers 

def extract_odd(lst):
    return [x for x in lst if x%2!=0]
print(extract_odd([10,11,12,13]))

