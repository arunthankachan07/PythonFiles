
#multiple inheritance
class Parent:
    def m1(self):
        print("parent method")

class Child():  # child class inherits proprties of parent class
    def m2(self):
        print("child method")


class Subchild(Child,Parent):  #multiple... inherits more than one classes
    def m3(self):
        print("sub child method")


ch = Child()
ch.m1()
ch.m2()