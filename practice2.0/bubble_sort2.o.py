def bubble_sort(list2):
    for i in range(len(list2)-1):
        for j in range(len(list2)-1):

            if list2[j] > list2[j+1]:
                temp = list2[j]
                list2[j] = list2[j+1]
                list2[j+1] = temp

        return list2
    
list2 = [10,12,15,16,18,9]

print("Unsorted list", list2)
print("sorted list: ", bubble_sort(list2))
