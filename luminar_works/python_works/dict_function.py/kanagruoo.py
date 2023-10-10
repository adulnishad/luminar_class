source_word="chicken"
target_word="hen"
source_word_list=[]
kangaroo_string=""


for ch in source_word:
    
        source_word_list.append(ch)
    
for ch in target_word:
    if ch in source_word_list:
        source_word_list.remove(ch) 
        kangaroo_string+=ch 
print(kangaroo_string==target_word)