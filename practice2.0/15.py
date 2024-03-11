list7 = ["apple","mango","grapes","onion"]
list7.append("aspish")
print(list7)


country = ["India", "Australia","Nepal","pAKISTAN"]
capital = ["Delhi","canberra","Kathmandu","Islamabad"]
country.extend(capital)
print(country)


country1 = ["India", "Australia","Nepal","pAKISTAN"]
capital2 = ("Delhi","canberra","Kathmandu","Islamabad")
country1.extend(capital2)
print(country1)


country1 = ["India", "Australia","Nepal","pAKISTAN"]
# capital2 = ("Delhi","canberra","Kathmandu","Islamabad")
country1.remove("India")

print(country1)


country1 = ["India", "Australia","Nepal","pAKISTAN"]
# capital2 = ("Delhi","canberra","Kathmandu","Islamabad")
country1.pop(1)

print(country1)


country1 = ["India", "Australia","Nepal","pAKISTAN"]
del country1


country1 = ["India", "Australia","Nepal","pAKISTAN"]
country1.clear()
print(country1)






