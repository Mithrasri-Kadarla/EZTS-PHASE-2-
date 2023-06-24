student_grade=[]
student_grade.append((1,"a"))
student_grade.append((4,"b"))
print("Yes")
print(student_grade)
student_grade.append((3,'c'))
student_grade.append((2,'d'))
student_grade.sort(reverse=True)
print("Priority wise sorted")
print(student_grade)
print("Original queue")
while student_grade:
    print(student_grade.pop())
    
