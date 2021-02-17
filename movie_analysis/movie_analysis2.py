moviedata=open("movies.csv", "r")
dict = {}
for data in moviedata:
    details = data.rstrip("\n").split(",")
    year=details[2]
    if year not in dict:
        # dict["movie_id"]=m_id
        dict[year]=1
    else:
        dict[year]+=1
print(max(dict,key=dict.get))
print(dict)
       # break