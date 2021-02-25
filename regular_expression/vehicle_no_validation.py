#vehicle number validation from file
import re
f=open("Vehicle_nos","r")
list1=[]
rule="[K][L]\d{2}[A-Z]{2}\d{4}"
for v_nos in f:
    number = v_nos.rstrip("\n")
    matcher = re.fullmatch(rule, number)
    if matcher != None:
        list1.append(number)
print(list1)

fw=open("vehnostore","w")
for num in list1:
    fw.write(num+"\n")
