text="hello hai how hello hai hai"
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(text)
print(dict)
data=sorted(dict,key=dict.get,reverse=True) #descending
print("Descending-",data)
data=sorted(dict,key=dict.get) #ascending
print("Ascending-",data)

