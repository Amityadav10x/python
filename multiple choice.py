eng_marks = int(input("enter marks for english :"))
math_marks = int(input("enter maths marks:"))

if(math_marks>80 and eng_marks>80):
    print("A grade")
elif(math_marks>80 or eng_marks>80):
    print("B grade")
else:
    print("c grade")