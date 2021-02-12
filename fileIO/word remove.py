f = open("demonews", "r")  # read file demo
dict = {}
stopwords=["\n","the","is","by","and","on","has","had","that","a","at","to","as"]
for lines in f:

    words = lines.rstrip("\n").split(" ")
    # print(words)
    for word in words:
        if word in stopwords:
            pass
        else:
            if word not in dict:
                dict[word]=1
            else:
                dict[word]+=1
print(dict)
print(max(dict,key=dict.get))