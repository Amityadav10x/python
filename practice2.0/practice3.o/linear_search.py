def linear_search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1

arr = [2, 30, 40, 60, 70]
x = 40
n = len(arr)

result = linear_search(arr, n, x)

if result == -1:
    print("Searched element not found.")
else:
    print("Searched element is found at index:", result)
