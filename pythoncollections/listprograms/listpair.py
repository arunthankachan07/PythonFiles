lst=[1,2,3,4]
element=int(input("Enter the elemnt"))
for i in lst:
    for j in lst:
        if((i+j==element)& (i!=j)):
            print(i,j)


