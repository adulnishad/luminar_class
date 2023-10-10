from re import *

variable=input("enter a variable name")

#rule="[a-aA-Z0-9]*"

#matcher=fullmatch(rule,variable)
#print("invalid" if matcher==None else "valid") 

# rule
# k,,,m
# must be a digit and that /by 3
# any number of characters
# 12-1 30
rule="[k-m][369][\w]*"

matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")
