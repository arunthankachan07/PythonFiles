# lst1=[1,2,3,4,5]
# lst2=[1,2,6,7,8]
# nlist=[]
# for i in lst1:
#     for j in lst2:
#         if(i==j):
#             nlist.append(i)
# print(nlist)


#me0thod 2
# lst1=[1,2,3,4,5]
# lst2=[1,2,6,7,8]
# nlist=[]
# for i in lst1:
#     for j in lst2:
#         if i==j:
#             nlist.append(i)
#         elif i>j:
#             j+=1
#         elif i<j:
#             i+=1
# print(nlist)


#method 3
lst1=[1,2,3,4,5,7]
lst2=[1,3,6,7,8]
pos1=0
pos2=0
while (pos1<len(lst1)) & (pos2<len(lst2)):

    if lst1[pos1]==lst2[pos2]:
        print(lst1[pos1])
        pos1+=1
        pos2+=1
    elif lst1[pos1]>lst2[pos2]:
        pos2+=1
    else:
        pos1+=1