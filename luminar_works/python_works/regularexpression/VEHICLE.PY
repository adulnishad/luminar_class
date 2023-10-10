 #



#start with kl
#2 digit
#alphabet min1 max 2
#digit 2

from re import *
vehicle_num=input("enter vehicle number")

rule="(KL)-[\d]{2}-[A-Z]{1,2}-[\d]{4}"

matcher=fullmatch(rule,vehicle_num)
print("invalid" if matcher==None else "valid")
