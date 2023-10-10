class hotel:
    items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"chickenrost","price":150},
    ]

    def create(self,*args,**kwargs):
        self.items.append(kwargs)
        return f"{kwargs}created"
    
    def retrive(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        return obj 
    def destroy(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0] 
        self.items.remove(obj)
        return f"{obj} has been removed"
    def update(self,id=None,*args,**kwargs):
        obj=self.retrive(id=id)
        obj.update(kwargs)
        return f"{obj} has been updated"   
obj=hotel()
#print(obj.create(id=106,name="noodels",price=180))
#print(obj.retrive(id=101))
#print(obj.destroy(id=102))
print(obj.update(id=102,name="VB"))



