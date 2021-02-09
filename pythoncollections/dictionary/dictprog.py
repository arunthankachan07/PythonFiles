student={"roll":1000,"name":"akhil","course":"MCA"}
print(student)
print(student["name"])  #accessing values in dictionary
if "total" in student:   #checking a key is present/not
    print("exist")
else:
    student["total"]=150   #adding values
print(student)

student["total"]+=50   #updating values
print(student["total"])

for item in student:
    print(item)