text="aabbcd"
#wc={}
#dup_lst=[]
#for ch in text:
#    if ch in wc:
  #      dup_lst.append(ch)
 #   else:
#        wc[ch]=1
#print(dup_lst[1])

non_lst=[]
dup_lst=[]

for ch in text:
    if ch in non_lst:
        dup_lst.append(ch)
    else:
        non_lst.append(ch)
print(dup_lst[1])