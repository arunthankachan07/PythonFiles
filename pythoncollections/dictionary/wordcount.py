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
maxval=max(dict,key=dict.get)
print(maxval)
print(maxval,"occurs",dict.get(maxval),"times")