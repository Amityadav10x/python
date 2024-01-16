

# Get user input for the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Check if the start is less than or equal to the end

if start <= end:
    print(f"nChecking even or odd for numbers in the range {start} to {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
else:
    print("Invalid range. The starting number should be less than or equal to the ending number.")
