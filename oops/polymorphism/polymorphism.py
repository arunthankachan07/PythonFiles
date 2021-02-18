#method overloading - only works recently added method
class Maths:
    def add(self):
        print("no arg method")
    def add(self,num1):
        print("1 arg method")
    def add(self,num1,num2):
        print("2 arg method")
math=Maths()


math.add(10,20)
math.add(10)
math.add()