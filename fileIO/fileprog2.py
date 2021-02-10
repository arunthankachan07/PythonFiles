f=open("demonews","r") #read file demo
names=set()
for lines in f:
    words=lines.rstrip("\n").split(" ")
    print(words)
    for word in words:
        names.add(word)
for word in words:
    print(word)