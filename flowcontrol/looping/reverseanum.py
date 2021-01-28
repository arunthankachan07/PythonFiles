num=int(input("Enter the num"))
reverse=0 #result=""
while(num!=0):
    reverse=num%10
    print(reverse) #result+=str(reverse)
    num//=10
#print(result)