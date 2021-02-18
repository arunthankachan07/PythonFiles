#method overriding -  create new definition
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self): #override method in object
        return self.name
p=Person("akhil",26)
print(p)