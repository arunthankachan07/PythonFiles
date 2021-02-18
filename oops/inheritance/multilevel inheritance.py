#multilevel inheritance
class Parent:
    def m1(self):
        print("parent method")

class Child(Parent): #child class inherits proprties of parent class
    def m2(self):
        print("child method")
class Subchild(Child):
    def m3(self):
        print("sub child method")
ch=Child()
ch.m1()
ch.m2()
#downward not possible
#ch.m3()

sb=Subchild()
sb.m3()
sb.m2()
sb.m1()


p=Parent()
p.m1()
#downward inheritation not possible
#p.m2()
#p.m3()