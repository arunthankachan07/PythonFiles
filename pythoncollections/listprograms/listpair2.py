lst=[1,2,3,4]
element=int(input("Enter the elemnt"))
low=0
upp=len(lst)-1
for i in range(0,len(lst)):
    sum=lst[low]+lst[upp]
    if sum==element:
        print("pairs",lst[low],lst[upp])
        low+=1
    elif sum<element:
        low+=1
    else:
        upp-=1

