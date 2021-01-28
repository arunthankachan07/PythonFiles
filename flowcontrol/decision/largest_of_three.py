
num1=int(input("Enter first num"))
num2=int(input("Enter second num"))
num3=int(input("Enter third num"))
if(num1>num2)&(num1>num3):
    print(num1,"is larger")
elif(num2>num3):
    print(num2,"is larger")
elif(num1==num2==num3):
    print("three numbers are equal")
else:
    print(num3,"is larger")

