# country1 = ["India", "Australia","Nepal","pAKISTAN"]
# for x in country1:
#     print(x)

# country1 = ["India", "Australia","Nepal","pAKISTAN"]
# for i in range(len(country1)):
#     print(country1[i])


country1 = ["India", "Australia","Nepal","pAKISTAN"]
list = []

for x in country1:
    if "A" in x:
        list.append(x)
        print(list)


country1 = ["India", "Australia","Nepal","pAKISTAN"]
newlist =  ["hello" for x in country1 ]
print(newlist)