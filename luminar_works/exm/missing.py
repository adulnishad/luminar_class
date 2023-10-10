lst=[1,2,3,5,6,7]
lst.sort()
for i in range(0,len(lst)-1):
       c=lst[i]
       n=lst[i+1]
       if(n-c!=1):
          print(f"{c+1} is the first positive missing integer")