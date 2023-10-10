#




#from re import*
#gmail_id=input("enter gmail id")
#rule="[a-z0-9][\w\w]+[@]gamil[.]com"
#matcher=fullmatch(rule,gmail_id)
#print("invalid" if matcher==None else "valid")

#password  
#rule-----
#atleast one uppercase
#atleast one special characters
# min of 8 characters
#

from re import *

password="Password@123"

rule="(?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,}"

matcher=fullmatch(rule,password)
print("valid" if matcher !=None else "in valid")

