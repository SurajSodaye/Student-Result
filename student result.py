name = input("Enter Your Name")
rollno = int(input("Enter your roll number"))
print("=== Enter Your 1st Semester Marks ===")
maths= int(input("Enter your maths marks"))
ml =int(input("Enter your Ml Marks"))
ai =int(input("Enter your AI Marks"))
r =int(input("Enter your R Marks"))
bd =int(input("Enter your Big Data Marks"))
print("=== Enter Your 2nd Semester Marks ===")
maths2= int(input("Enter your maths 2 marks"))
aml =int(input("Enter your advance Ml Marks"))
aai =int(input("Enter your advance AI Marks"))
py =int(input("Enter your Python Marks"))
ann =int(input("Enter your ANN Marks"))


total= maths + ml + ai + r + bd
total1= maths2+aml+aai+py+ann
percent = total/5
per = total1/5
sgpa = percent/10
sgpa1 = per/10
cgpa = sgpa + sgpa1/20

print("=== Student Result ===")
print("Student Name =", name)
print("Student Roll Number =", rollno)
print("=== 1st Semester ===")
print("Total Marks in 1st semester =", total)
print("Percentage in 1st Semester=", percent)
print("SGPA For Semester 1 =", round(sgpa,2))
if percent>=90:
    print("Grade Obtain in 1st semester = A")
elif 90>percent>=70:
    print("Grade Obtain in 1st semester = B")
elif 70>percent>=40:
    print("Grade Obtain in 1st semester = C")
else:
    print("You are Fail in 1st semester")
    
print("=== 2nd Semester ===")
print("Total Marks in 2nd semester =", total1)
print("Percentage in 2nd Semester=", per)
print("SGPA For Semester 2 =", round(sgpa1,2))
if per>=90:
    print("Grade Obtain in 2nd semester = A")
elif 90>per>=70:
    print("Grade Obtain in 2nd semester = B")
elif 70>per>=40:
    print("Grade Obtain in 2nd semester = C")
else:
    print("You are Fail in 2nd semester")


print("CGPA =", round(cgpa,2))



                    
            
            
