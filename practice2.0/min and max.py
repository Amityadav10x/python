arr = [10, 12, 13, 134, 12, 13, 17, 19, 43]

min_val = arr[0]
max_val = arr[0]

for i in range(len(arr)):
    if arr[i] < min_val:
        min_val = arr[i]
    if arr[i] > max_val:
        max_val = arr[i]

print("Minimum is", min_val)
print("Maximum is", max_val)
