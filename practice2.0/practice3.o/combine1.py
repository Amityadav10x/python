# Bubble sort 

def bubble_sort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):

            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp 

    return list1
    
list1 = [10,20,30,70,60]

print("Unsorted list is :",list1)
print("sorted list is :",bubble_sort(list1))


# linear_search 

def linear_search(arr,x,n):
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1
    
arr = [10,23,24,35,22,24,56,75,45]
x = 75
n = len(arr)

result = linear_search(arr,x,n)

if result == -1:
    print("searched element not found.")
else:
    print("searched element found at index",result)

