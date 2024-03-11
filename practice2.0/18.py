list = ["apple","mango","grapes","onion"]
list1 = list.copy()
print(list1)

list = ["apple","mango","grapes","onion"]
list1 = [1,2,3,4,5,6,7,8]
list3 = list+list1
print(list3)

list = ["apple","mango","grapes","onion"]
list1 = [1,2,3,4,5,6,7,10]

for x in list:
    list1.append(x)
    print(list1)

list = ["apple","mango","grapes","onion"]
list1 = [1,2,3,4,5,6,7,8]

list.extend(list1)
print(list)