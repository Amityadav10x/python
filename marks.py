marks = int(input("enter marks of students:"))

if(marks>80):
    print("very good")
elif(marks<80 and marks>60):
    print("good")
elif(marks<60 and marks>40):
    print("average")
elif(marks<40):
    print("fail")
else:
    print("no seated in the exam")