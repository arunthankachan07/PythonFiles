import  re
rule='\w+[@]gmail.com'   #\w{6,30}
var_name=input("Enter a gmail id")
matcher=re.fullmatch(rule,var_name)   #apply the pattern to all of the string... returning a match object...or none if no match
if matcher==None:
    print("Invalid id")
else:
    print("Valid")