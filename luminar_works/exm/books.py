data=[
    {"id":100,"name":"python","price":350},
    {"id":101,"name":"java","price":450},
    {"id":102,"name":"django","price":1350},
    {"id":103,"name":"html","price":1250},
    {"id":104,"name":"boostrap","price":550},
]
booknames=[i.get("name") for i in data]
print(booknames)
# b
price=[i.get("price") for i in data if i.get("name")==("java")]
print(price)
# c
update=[]