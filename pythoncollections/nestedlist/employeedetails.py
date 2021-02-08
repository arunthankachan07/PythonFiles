employees=[[100,"akhil","developer","50000",1989,1995],
           [101,"anu","developer","45000",1970,1990],
           [102,"aby","qa","30000",1989,1991],
           [103,"james","qa","35000",1990,1999]]
highexp=[]
#employees worked in 90s
for emp in employees:
    if emp[4] & emp[5] in range(1990,1999):
        print(emp)

#exp of each employee
for emp in employees:
    exp=emp[5]-emp[4]
    print(emp[1],exp,"years")

#highest exp
for emp in employees:
    exp = emp[5] - emp[4]
    highexp.append(exp)
high=max(highexp)
print(high)
for emp in employees:
    exp=emp[5]-emp[4]
    if(high==exp):
        print(emp)


