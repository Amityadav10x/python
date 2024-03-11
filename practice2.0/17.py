# country1 = ["India", "Australia","Nepal","pAKISTAN"]
# country1.sort()
# print(country1)

# country1 = [12,32,44,45,223,343,22]
# country1.sort()
# print(country1)


# country1 = ["India", "Australia","Nepal","pAKISTAN"]
# country1.sort(reverse=True)
# print(country1)

# country1 = [12,32,44,45,223,343,22]
# country1.sort(reverse=True)
# print(country1)

# def myfunc(n):
#     return abs(n-60)
# country1 = [12,32,44,45,223,343,22]
# country1.sort(key=myfunc)
# print(country1)


# name = ["amit","sumit","shyam","vijay"]
# name.sort()
# print(name)


name = ["amit","Sumit","shyam","vijay"]
name.sort(key=str.upper)
print(name)


name = ["amit","Sumit","shyam","vijay"]
name.reverse()
print(name)