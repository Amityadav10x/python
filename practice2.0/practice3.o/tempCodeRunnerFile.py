
def linear_search(arr,x,n):
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1
    
arr = [10,23,24,35,22,24,56,75,45]
x = 75