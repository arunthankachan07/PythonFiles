#print prime numbers in the list
low=int(input("Enter the lower limit:"))
limit=int(input("Enter the limit:"))
for i in range(low,limit+1):
    if(i>1):
        for j in range(2,i):
            if (i % j==0):
                break
        else:
            print(i)