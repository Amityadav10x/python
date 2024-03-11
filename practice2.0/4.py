def calculate_grades(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks <80:
        return "B+"
    elif 60 <= marks <70:
        return "B"
    elif 50 <= marks <60:
        return "C"
    elif 40 <= marks <50:
        return "D"
    else:
        return "Fail"

marks = float(input("Enter marks: "))
grade = calculate_grades(marks)
print("Grade:", grade)