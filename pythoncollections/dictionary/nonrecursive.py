st='ABABAC'
dit={}
for ch in st:
    if ch not in dit:
        dit[ch]=1
    else:
        dit[ch]+=1
print(dit)
print(min(dit,key=dit.get))


for k,v in dit.items():    #both key and values are taken
    if v==1:
        print(k)
