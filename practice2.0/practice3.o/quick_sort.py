
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
     
    pivot = arr[len(arr) //2]

    left  = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [10,12,41,5,56]

sorted_array   = quick_sort(arr.copy())

print("after applying quick_sort we will get", sorted_array)


