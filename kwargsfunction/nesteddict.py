#nested dictionary
students={
    1000:{"id":1000,"name":"akhil","course":"django","qualification":"btech"},
    1001:{"id":1001,"name":"sukesh","course":"django","qualification":"btech"},
    1002:{"id":1002,"name":"jamsheer","course":"django","qualification":"btech"},
    1003:{"id":1003,"name":"nikhil","course":"django","qualification":"btech"},
    1004:{"id":1004,"name":"gokul","course":"django","qualification":"mca"},


}
print(students[1000]) #print students details of id 1000
print(students[1000]["name"]) #print name from students id  1000


id=int(input("enter student id"))
if id in students:
    property = input("enter property")
    if property in students[id]:
        print(students[id]["name"],students[id][property])
    else:
        print(students[id]["name"]," ",property," not found")
else:
    print("id not found")
