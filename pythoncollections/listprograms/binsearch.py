arr=[20,11,8,13,22,15,6,18]
element=int(input("Enter an element"))
def binsearch(arr,element):
    arr.sort()
    low = 0
    upp = len(arr) - 1
    while low<=upp:
        mid=(low+upp)//2
        if(element==arr[mid]):
            return mid
        elif(element<arr[mid]):
            upp=mid-1
        elif(element>arr[mid]):
            low=mid+1
    return -1
res=binsearch(arr,element)
if(res==-1):
    print("Number not found")
else:
    print("Number found at position",str(res))