class Student:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.marks=total
st=Student(100,"arun","mca",400)
st1=Student(101,"aby","bca",340)
st2=Student(102,"joel","bca",300)
st3=Student(103,"aju","mca",350)

students=[]
students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)
mark=[]
map()

for student in students:


    # if student.course=="mca":
    #     print(student.name)
    mark.append(student.marks)
print(max(mark))