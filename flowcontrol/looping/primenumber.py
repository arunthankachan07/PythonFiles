#prime number
num=int(input("Enter the num"))
f=0
for i in range(2,num):
    if(num%i==0):
        f=1 #break
    else:
        f=0  #pass
if(f==1):
    print("Not prime")
else:
    print("Prime")
