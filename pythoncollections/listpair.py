lst=[1,2,3,4]
element=int(input("Enter the elemnt"))
flag=0
for i in lst:
    for j in lst:
        if((i+j==element)& (i!=j)):
            flag=1
            break
        else:
            flag=0
if(flag==1):
    print(i,j)
else:
    print("no pairs found")

