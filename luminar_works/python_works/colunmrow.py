# for row in range(1,4):
#     for col in range(row):
#         print("#",end="\t")
#     print()



# for row in range(1,5):
#     for col in range(row):
#         print(col+1,end="\t")
#     print()


# 1
# 1       #
# 1       #       3
# 1       #       3       #
# 1       #       3       #       5
# 1       #       3       #       5       #


# for row in range(1,7):
#     for col in range(row):
#         val=col+1
#         if val %2==0:
#           print("#",end="\t")
#         else:
#            print(val,end="\t")
#     print()





# for row in range(5,0,-1):
#      for col in range(row):
#          print("#",end="\t") 
#      print()

for row in range(1,7):
      for sp in range(row-1,-1):
         print(" ",end=" ")
      for col in range(row):
          print("*",end="")    
      print()

