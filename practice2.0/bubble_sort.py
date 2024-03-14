def bubble_sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1):

            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp

    return list1

list1 = [2, 8, 3, 4, 6]

print("Unsorted list is ", list1)
print("Sorted list is ", bubble_sort(list1))




