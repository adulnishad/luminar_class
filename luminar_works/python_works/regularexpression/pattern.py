from re import *


# text="chetta 2 coffeABC@"
# pattern="[a-z0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())



# text="chetta 2 coffeABC@"
# pattern="[a-zA-Z0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())    

# text="chetta 234 coffeABC@"
# pattern="\d" #[0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
    # print(m.start(),m.group())

    # exclude digits

# text="chetta2coffeABC@"
# pattern="\D"
# matcher=finditer(pattern,text)
# for m in matcher:
    # print(m.start(),m.group())

    # alaphets and unit number

# text="chetta 2 coffeABC@"
# pattern="\w"        #[a-zA-Z0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
    # print(m.start(),m.group())

    # special characters

text="chetta2coffeABC@"
pattern="\W"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())