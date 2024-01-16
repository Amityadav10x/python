def maximum(val1, val2, val3):
    if val1 > val2 and val1 > val3:
        print("Value 1 is the maximum:", val1)
    elif val2 > val1 and val2 > val3:
        print("Value 2 is the maximum:", val2)
    elif val3 > val1 and val3 > val2:
        print("Value 3 is the maximum:", val3)
    else:
        print("Entered a wrong value")

val1 = 10
val2 = 15
val3 = 5

maximum(val1, val2, val3)
