# users=["mamooty","mohanlal","dileep","dq","fahad","kb"]
# dileep_friends=["mohanlal","kb","dq"]

# for u in users:
#     if u not in dileep_friends:
#         print(u)
        
arr=[5,3,1,2,5,7,5]
arr.sort()

for i in range(0,len(arr)-1):
    current=arr[i]
    next=arr[i+1]
    if current==next:
        print(current)
