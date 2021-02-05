#print even numbers in the list
lst=[3,4,6,7]
for num in lst:
    if(num%2==0):
        print(num)


#print odd and even numbers in separate list
elist=list()
olist=list()
for num in lst:
    if num%2==0:
        elist.append(num)
    else:
        olist.append(num)
print(elist)
print(olist)