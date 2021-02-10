f=open("demo","r") #read file demo
names=set()
list=[]
for lines in f:
    #list.append(lines) #store values in file to list (default value stored with \n)
    list.append(lines.rstrip("\n"))
    names.add(lines.rstrip("\n"))  # store values in file to list
    #rstrip is used to strip from right side of data
print(list) #list
print(names) #set