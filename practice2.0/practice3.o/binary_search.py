def binary_search(arr,target):

    low = 0
    high = len(arr) -1 

    while low <= high:
        mid = (low + high)  // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid -1

    return -1 

arr = [10,12,13,14,15,16]
target = 13

result = binary_search(arr,target)

if result != -1:
    print(f"value found at index {result}")
else:
    print("value not found !")
        