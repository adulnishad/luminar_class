f=open("C:\\Users\\VICTUS\\OneDrive\\Desktop\\adulpy\\fileoperations\\data.txt","r")

words=[line.rstrip("\n") for line in f]
print(words)

