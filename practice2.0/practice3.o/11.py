def week_days(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4 :
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "sunday"
    else:
        return "given day is invalid"
print(week_days(10))