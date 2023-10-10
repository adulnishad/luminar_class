from re import *


text="aaaabbbaaa"
      #0123456789
# pattern="a+"  #+ one more or more a
# pattern="b*"  #zero or more ooccurance of a
pattern="a{1,2}" #minimum and maximum
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())