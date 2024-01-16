

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start <= end:
    
    print("Numbers in the range:")
    for num in range(start, end + 1):
        print(num)
else:
    print("Invalid range. The starting number should be less than or equal to the ending number.")
