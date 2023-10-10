source_word="decreases"
target_word="dress"

wc={}

for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for ch in  target_word:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1
    else:
        print("not in kangaroo")
        break