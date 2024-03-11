eng_marks = int(input("enter marks of english :"))
math_marks = int(input("enter marks of math :"))
hindi_marks = int(input("enter marks of hindi :"))
comp_marks = int(input("enter marks of comp :"))
dld_marks = int(input("enter marks of dld :"))

if(hindi_marks<80 and hindi_marks>50):
    print("student is good in hindi")

elif(math_marks<75 and math_marks>33):

    print("student is good in maths")

elif(comp_marks<80 and comp_marks>45):
    print("student is good in comP")

elif(dld_marks<65 and comp_marks>35):
    print("student is good in dld")
else:
    print("student is a average student")