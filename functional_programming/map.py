#map function
lst=[2,4,6,7]
squares=list(map(lambda num:num**2,lst))
print(squares)

#upper case
lit1=["ajay","nelvin","akhil","arun"]
upp=list(map(lambda name:name.upper(),lit1))
print(upp)

numbers=[4,6,8,9,3,2]
func=list(map(lambda num:num+1 if num>5 else num-1,numbers))
print(func)

list2=[40,52,30,60,70]
check=list(map(lambda num:"P" if num>50 else "F",list2))
print(check)