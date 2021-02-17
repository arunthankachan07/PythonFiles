#oject oriented programming
#create class
class Person:  #class name starts with caps
    bank_name="SBI"   #class variable/static variable
    def set_values(self,name,age):   #method (variables inside method are local variables
        self.name=name  #self.name, self.age---instance variables
        self.age=age
    def print_values(self):
        print(self.name)
        print(self.age)
        print(Person.bank_name)

#create object
obj=Person()    #Ref_name=class_name()
obj.set_values("akhil",27)
obj.print_values()
#print(Person.bank_name)

# obj1=Person()
# obj1.set_values("arun",26)
# obj1.print_values()