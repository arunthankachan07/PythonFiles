#regular expression
import re
pattern="ab"  #---matches exact 'ab'
matcher=re.finditer(pattern,"abababbbbabab")
count=0
for match in matcher:
    print(match.start()) #gives the position of match
    print(match.group()) #gives the object that matches
    count+=1
print("total matches:",count)