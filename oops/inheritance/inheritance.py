#single inheritance
class Parent:
    def phone(self):
        print("phone method")
    def __str__(self):
        print("")
class Child(Parent): #child class inherits proprties of parent class
    pass
ch=Child()
ch.phone()
print(ch)