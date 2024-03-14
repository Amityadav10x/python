# linear search

def linear_search(arr, x, n):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
         
    
arr = [10,30,67,80,97,56]
x = 80
n = len(arr)
    
result = linear_search(arr,x,n)

if result == -1 :
    print("searched element is not found")
else:
    print("searched element is found at index ",result)
        

#bubble sort
    

def bubble_sort(list3):
    for i in range(len(list3)-1):
        for j in range(len(list3)-1):

            if list3[j] > list3[j+1]:
                temp = list3[j]
                list3[j] = list3[j+1]
                list3[j+1] = temp

        return list3
    
list3 = [10,20,40,500,60]
print("unsorted array :",list3)
print("sorted array is : ",bubble_sort(list3))


      