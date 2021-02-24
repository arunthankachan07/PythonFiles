#regular expression
import re
#predifend character set
#--------------------------------
pattern='[abc]' #---matches either 'a', 'b' or 'c'
pattern='[a-z]'   #---checks lower case a to z
pattern='[A-Z]'     #----checks upper case A to Z
pattern='[a-zA-Z]'  #-----checks both lower and upper cases a to z, A to Z
pattern='[0-9]'   #-----matches digits
pattern='[a-zA-Z0-9]'   #---both lower,upper,digits
pattern='[^a-zA-Z0-9]'  #----except all


#predifend character
#----------------------
pattern="\s"  #---space
pattern="\d"   #----digits
pattern="\D"   #---except digits
pattern="\w"    #---all words
pattern="\W"    #---special characters

matcher=re.finditer(pattern,"abc _ZK7@")
for match in matcher:
    print(match.start(),match.group()) #gives the position of match
    #print(match.group()) #gives the object that matches

