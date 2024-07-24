student_mark = []
student_name = []

for i in range(3):
    for j in range(5):
        student_mark.append(int(input(f"Enter student Mark {j}: ")))

    for k in range(1):
        student_name.append(input("Enter student name: "))

print("2nd Student Marks is " + str(student_mark) + " , 2nd Student name " + str(student_name))
