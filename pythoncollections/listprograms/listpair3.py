lst1=[1,2,3,4,5]
lst2=[1,2,6,7,8]
nlist=[]
for i in lst1:
    for j in lst2:
        if(i==j):
            nlist.append(i)
print(nlist)