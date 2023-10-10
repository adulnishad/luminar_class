text="ABCABCS"
wc={}
for ch in text:
    if ch in wc:
        print(ch,"is the first recrusive character")
        break
    else:
     wc[ch]=1