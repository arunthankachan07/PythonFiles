num=int(input("Enter the num"))#123
reverse=0
while(num!=0):
    reverse=num%10
    print(reverse)
    num//=10
