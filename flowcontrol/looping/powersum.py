num=int(input("Enter the num"))#123
reverse=0
sum=0
while(num!=0):
    reverse=num%10
    sum=(reverse**3)+sum
    num//=10
print(sum)