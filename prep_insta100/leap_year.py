year  = 1000
if (year % 4 == 0) or (year % 400 == 0 and year % 100!=0):
    print("year is a leap year")
else:
    print("year is not a leap year")




def leap_year(year):
    if (year % 4 == 0) or (year % 400 == 0 and year % 100!=0):
        return " leap year"
    return " not a leap year"

year = 2000

print(leap_year(year))

