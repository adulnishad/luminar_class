f=open("C:\\Users\\VICTUS\OneDrive\\Desktop\\adulpy\\fileoperations\\years.txt","r")
# for line in f:
#     print(line)


for years in f:
    years=int(years)

    if (years %100==0) and (years %400==0):
        print(f)
    elif(years %100!=0)and(years %4==0):
        print(f)    