items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},

]


# def add_item(*args,**kwargs):
    
#     items.append(kwargs)

# add_item(id=106,name="bb",price=160)
# print(items)


# def retrive_item(id=None,*args,**kwargs):
#     obj= [i for i in items if i.get("id")==id]

#     return obj
# print(retrive_item(id=102))

    
# def destroy_item(id=None,*args,**kwargs):
#     obj= [i for i in items if i.get("id")==id][0]
#     items.remove(obj)

# destroy_item(id=103)
# print(items)  


def update_item(id=None,*args,**kwargs):
    obj= [i for i in items if i.get("id")==id][0]
    obj.update(kwargs)
update_item(id=102,name="chappati")   
print(items)



    # c create  r retrive  u update   d delete  (crud) 