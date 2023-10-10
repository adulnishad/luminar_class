from re import *
f=open("C:\\Users\\VICTUS\\OneDrive\\Desktop\\adulpy\\regularexpression\\data.text")
phone_rule="\d{10}"
mail_idrule="[a-z][\w\W]+[@]gmail[.]com"
mail_ids=[]
phone_numbers=[]



for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        p_matcher=fullmatch(phone_rule,w)
        e_matcher=fullmatch(mail_idrule,w)
        if p_matcher!=None:
            phone_numbers.append(w)
        elif e_matcher!=None:
            mail_ids.append(w)

print(phone_numbers)
print(mail_ids)

