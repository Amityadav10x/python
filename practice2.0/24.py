# second largest element

def second_largest(lst):
    unique_sorted = sorted(set(lst))
    if len(unique_sorted) < 2:
        return "list have 2 element"
    return unique_sorted[-2]
print(second_largest([10,23,44,33,56]))