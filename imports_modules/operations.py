#METHOD 1
#import functions from another modules
import MathModule #import module_name
addres=MathModule.add(100,200) #module_name.function_name(arguments)
print(addres)
subres=MathModule.sub(500,200)
print(subres)
mulres=MathModule.mul(50,30)
print(mulres)
divres=MathModule.div(100,50)
print(divres)


#METHOD 2
from MathModule import *  #Syntax: from module_name import *
print(add(100,200))
print(sub(200,100))
print(mul(10,200))
print(div(200,10))


#METHOD 3
import MathModule as np   #Syntax: import Module_name as alias_name
addres=np.add(100,200)    #alias_name.function_name(arguments)
print(addres)


#Syntax for importing from another directory
#import directory_name.module_name as alias_name