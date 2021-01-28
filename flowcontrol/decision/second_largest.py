num1=int(input("Enter first num"))
num2=int(input("Enter second num"))
num3=int(input("Enter third num"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2,"is larger")
    else:
        print(num3,"is larger")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print(num1,"is larger")
    else:
        print(num3,"is larger")
elif(num3>num1)&(num3>num2):
    if (num1 > num2):
        print(num1, "is larger")
    else:
        print(num2, "is larger")
