#variable name
#rules
#1. start with a-k
#2. second character should be a digit and divisible by 3
#3. any number of characters

import  re
#rule='[a-k][369][a-zA-Z]*'
rule="[K][L]\d{2}[A-Z]{2}\d{4}"
rule="[6-9]\d{9}"
var_name=input("Enter a variable name")
matcher=re.fullmatch(rule,var_name)   #apply the pattern to all of the string... returning a match object...or none if no match
if matcher==None:
    print("Invalid variable name")
else:
    print("Valid variable name")