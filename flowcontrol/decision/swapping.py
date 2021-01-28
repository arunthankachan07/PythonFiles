num1=int(input("Enter first num"))
num2=int(input("Enter second num"))
num3=int(input("Enter third num"))
small = 0
middle = 0
large = 0
if(num1<num2)&(num1<num3):
    small=num1
    if(num2<num3)&(num2<num1):
    small=num2
    else:
    small=num3
elif(num1<num2)&(num1<num3):
    middle=num1
    if(num2>num1)&(num2<num1):
    middle=num2
    else:
    middle=num3
elif(num1>num2)&(num1>num3):
    large=num1
    if(num2>num3)&(num2>num1):
    large=num2
    else:
    large=num3
print("sorted order:",small,middle,large)