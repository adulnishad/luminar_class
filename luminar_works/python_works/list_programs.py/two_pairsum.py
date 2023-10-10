list=[2,3,4,5]
sum=8
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        cur_sum=list[i]+list[j]
        if cur_sum==sum:
            print("pair",list[i],list[j])
            count=+1
            print(count)


