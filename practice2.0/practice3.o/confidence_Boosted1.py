def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)// 2]

    left = [  x for x in arr if x < pivot ]
    middle = [ x for x in arr if x == pivot ]
    right = [ x for x in arr if x > pivot]

    return quick_sort(right) + middle + quick_sort(left)

arr = [10,23,12,141,5]

sorted_array = quick_sort(arr.copy())

print("sorted array_is", sorted_array)
