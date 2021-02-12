coviddata = open("covid_19_india.csv", "r")
dict = {}
for data in coviddata:
    words = data.rstrip("\n").split(",")
    #print(words)
    state=words[3]
    confirmed_cases=words[-1]
    if state not in dict:
        dict[state]=int(confirmed_cases)
    else:
        dict[state]=int(confirmed_cases)
    # print(dict)
for k,v in dict.items():
    print(k," ",v)
print("highest-",max(dict,key=dict.get))
print("Lowest-",min(dict,key=dict.get))