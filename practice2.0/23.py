# second  smallest element

def second_smallest(lst):
    unique_sorted  = sorted(set(lst))
    if len(unique_sorted) < 2:
        return "list have fever than 2 element"
    return unique_sorted[1]

print(second_smallest([10,12,13,14,15]))

# 2nd maximum

def third_smallest(lst):
    Unique_sorted = sorted(set(lst))
    if len(Unique_sorted) < 3:
        return "list has fever than 3 element"
    return Unique_sorted[-2]

print(third_smallest([10,12,13,17,34]))

