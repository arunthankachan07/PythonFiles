num=int(input("Enter a number")) #2
low=int(input("Enter the lower limit")) #1
limit=int(input("Enter the upper limit")) #10

for i in range(1,limit+1):
    res = i ** num
    for j in range(low,limit+1):
        if(res==j):
            print(res)


