#print pairs
lst=[1,2,3,4]
num=7
st=set(lst)
for no in lst:
    res=num-no
    if res in st:
        print(no,res)