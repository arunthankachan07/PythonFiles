moviedata=open("BollywoodMovieDetail.csv", "r")
dict = {}
for data in moviedata:
    details = data.strip("\n").split(",")
    title=details[1]
    year=details[2]
    if title not in dict:
        # dict["movie_id"]=m_id
        dict[title]=year
    else:
        pass
for k,v in dict.items():
        print(k,"",v)
       # break


