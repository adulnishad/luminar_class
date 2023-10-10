text="aeiouhsksplj"
for ch in text:
    v_count=0
    c_count=0
    if ch in ["a","e","i","o","u"]:
         v_count+=1
    else:
         c_count+=1
         print("vowel count",v_count)
         print("constant count",c_count)
    