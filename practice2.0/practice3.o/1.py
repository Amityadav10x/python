def positive_number(num):
    if(num>0):
        return "Number is positive"
    return " number is negative"
print(positive_number(num=1))




arr = [10,20,30,40,50,60]

from array import array

arr = array("i",[10,203,405,32])

max_value = max(arr)
min_value = min(arr)

print("maximum value is :" , max_value)
print("Minimum value is :", min_value)




arr = [10,20,40,60,70,90]

max_value = arr[0]
min_value = arr[0]

for num in arr :
    if num > max_value:
        max_value = num
    elif num < min_value:
        num = min_value
print("Maximum value is :", max_value)
print("Minimum value is :",min_value)

