#function overloading
def add(num1,num2):
    return num1+num2

def add(num1,num2,num3):
    return num1+num2+num3
print(add(10,20,30))  #works recent added function
#print (add(10,20)) #not works

#*num -> assign any number of values

def add(*num):  #assign any number of arguments
    print(num)
    print(sum(num))
    print(max(num))
add(10,20,30,40)  #takes values in tuple format


def emp_det(*args): #*tuple format
    print(args)
emp_det(100,"ajay","kakkanad","thrissur")

def emp_deta(**args):  #** dictionary format
    print(args)
emp_deta(id=100,name="ajay",location="kakkanad",home="thrissur")