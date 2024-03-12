# reverse the list

def reverse_list(lst):
    lst.reverse()

my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print(my_list)


# sorting the list

def sort_list(st):
    st.sort()

my_list = [10,11,13,16,15]
sort_list(my_list)
print(my_list)


# removing duplicates 

def del_duplicates(dlt):
    return list(set(dlt))

print(del_duplicates([12,12,34,32,23,33]))