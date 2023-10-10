f=open("C:\\Users\\VICTUS\\OneDrive\\Desktop\\adulpy\\fileoperations\\numbers.txt","r")

all_number=[line.rstrip("\n") for line in f]
print(all_number)


kerala_nums=[num for num in all_number if num.startswith("kl")]
print(kerala_nums)



# read from years  r
# write leap years in to lepyear.txt  l_w  w
# write nonleap years in to nonlepyear.txt nl_w  w