arr=[10,11,12,13,14,15,16,18]
element=int(input("Enter an element"))
res=0
for num in arr:
    if(element==num):
        res = res+1
if(res==1):
    print("element is present")
else:
    print("element is not present")