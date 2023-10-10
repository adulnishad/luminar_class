# print all vowels

from re import *

text="goodmorning"

# pattern="[aeiou]"
pattern="[^aeiou\W\d]" #exclude vowels
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())