def bubble_sort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):

            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp 

    return list1


list1 = [10,12,13,16,19]

print("Unsorted list",list1)
print("Sorted list", bubble_sort(list1))



            