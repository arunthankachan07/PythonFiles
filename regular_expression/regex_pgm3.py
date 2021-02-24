import re
pattern="a+"  #---matches consecutive a  (one or more a)
pattern="a*"   #---any number of a including 0
pattern="a{2}"   #---2 number of a's
pattern="a{2,3}"   #----minimum 2 maximum 3
matcher=re.finditer(pattern,"aaaaaabbbbaaaabaab")
for match in matcher:
    print(match.start(),match.group()) #gives the position of match
    #print(match.group()) #gives the object that matches
