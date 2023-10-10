# first three characters must be  upper case  random alphabet 
#4th palce must be alphabets(PCFHTA)
#5TH place any random upper case alphabet
#4 digit 
#one alphabet

from re import*
pan_num=input("enter the pancard number:>")

rule="[A-Z]{3}[PCFHTA]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"

matcher=fullmatch(rule,pan_num)
print("invalid" if matcher==None else "valid")
