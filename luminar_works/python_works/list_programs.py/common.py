lst1=[10,12,12,13,16]
lst2=[12,13,14,20,21]
#out=[]


#for n1 in lst1:
    #if n1 in lst2:
    #    print("common",n1)
 #method2
 
lst1.sort()
lst2.sort()
p1,p2=0,0

while(p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print("common",lst2[p2])
        p2+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1
    else:p2+=1
