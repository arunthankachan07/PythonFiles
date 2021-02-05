s='ABABC'
l=len(s)
# count=0
for i in range(0,l):
    k=i+1
    for j in range(k,l):
        if(s[i]==s[j]):
            # count+=1
            print(s[i])

    # k=i+1
    # for j in range(k,l):
    #     if str[i]==str[j]:
    #         print(i)

