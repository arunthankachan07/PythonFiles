#num2=2+22
num=int(input("Enter the num"))
sum=0
for i in range(1,(num+1)):
    a=str(num)*i
    sum=sum+int(a)
print(sum)