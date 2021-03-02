#functional programming : list comprehension

#prog1: print squares
lst=[1,2,3,4]
op=[num**2 for num in lst]
print(op)

#prog2: even numbers from list
even=[num for num in lst if num%2==0]
print(even)

#prog3: common elements
lst1=[1,2,3]
lst2=[3,4,5]
com=[num for num in lst1 if num in lst2]
print(com)

#prog4: print pairs
lst3=[1,2,3]
lst4=[4,5,6]
pairs=[(num3,num4) for num3 in lst3 for num4 in lst4 ]
print(pairs)

#prog5: list of list
lst5=[[10,20],[30,40],[50,60]]
new_list=[num for num1 in lst5 for num in num1]
print(new_list)

#prog6:
lst6=[4,3,2,5,6,7,8]
new_list1=[num+1 if num>5 else num-1 if num<5 else 5 for num in lst6 ]
print(new_list1)

#prog7:
lst5=[[10,20],[20,30],[30,40]]
new_list=[num for num1 in lst5 for num in num1]
print(sorted(set(new_list)))

