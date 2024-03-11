def max_of_two(x,y):
    if(x>y):
        return x
    return y
print(max_of_two(2,5))

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

print(max_of_three(3,4,5))
    