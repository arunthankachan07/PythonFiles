population={"ind":100,"china":200,"nz":40,"aus":35}
data=sorted(population) #sort using key---default
print(data)
dat=sorted(population,key=population.get) #get is used to access value--- sort using values---ascending order
print(dat)
dat=sorted(population,key=population.get,reverse=True) #sort using values---descending order
print(dat)
