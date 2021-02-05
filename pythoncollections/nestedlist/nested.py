#nested list
employees=[[100,"akhil","developer","50000",1989,1995],
           [101,"anu","developer","45000",1970,1990],
           [102,"aby","qa","30000",1989,1991],
           [103,"james","qa","35000",1990,1999]]
sum=0
sallist=[]
for emp in employees:
    #print(emp[1]) #print emp names
    #print(emp[4]) #print emp salaries
   # if(emp[2]=='developer'): #print developer details
    #    print(emp)

#     sal=int((emp[4]))
#     sum=sum+sal
# print(sum)  #sum of salary

    sallist.append(int(emp[4]))
print(max(sallist))   #maximum value

