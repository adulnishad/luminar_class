text="hi bye goodmorning hello zython"

words=text.split(" ")

# l_word=max(words,key=lambda w:len(w))
# print(l_word)
 
srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt) 
