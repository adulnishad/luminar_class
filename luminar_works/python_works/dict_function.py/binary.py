


# data structure and algorithm(dsa)

# leaner search
# binary search
# word count
# first recrusive
#  sort
# bubble sort
# quick sort
# merge sort
# dfs(depth first search)
# bfs(birth first search)
# dijkstra algorithm



#binary search
#worst case= non\t number
#edge case


lst=[12,3,4,15,16,18]
lst.sort()
element=180
low=0
upp=len(lst)-1
is_found=False
while(low<=upp):
    mid=(low+upp)//2
    if element==lst[mid]:
        is_found=True
        break
    elif element<lst[mid]:
        upp=mid-1
    elif element>lst[mid]:
        low=mid+1
print(is_found)

