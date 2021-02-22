class Student:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.marks=total
    def __str__(self):
        return self.name
st=Student(100,"arun","mca",400)
st1=Student(101,"aby","bca",340)
st2=Student(102,"joel","bca",300)
st3=Student(103,"aju","mca",350)
#student=[st,st1,st2,st3]
students=[]
students.append(st)
students.append(st1)
students.append(st2)
students.append(st3)
mark=[]

#print student name upper
upp=list(map(lambda stud:stud.name.upper(),students))
print(upp)
#add 50 bonus mark
bonusmark=list(map(lambda stud:stud.marks+50,students))
print(bonusmark)

#print student name, course = mca
mca_stud=list(map(lambda st:st.name,list(filter(lambda stud:stud.course=='mca',students))))
print(mca_stud)

#maximum mark
max_marks=max(list(map(lambda st:st.marks,students)))
print(max_marks)

#minimum marks
min_marks=min(list(map(lambda st:st.marks,students)))
print(min_marks)
#str method
# for stud in mca_stud:
#     print(stud)
# mca=list(map(lambda stud:stud.name,mca_stud))
# print(mca)








# for student in students:
#
#
#     # if student.course=="mca":
#     #     print(student.name)
#     mark.append(student.marks)
# print(max(mark))