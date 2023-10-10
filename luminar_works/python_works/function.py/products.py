items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
    
]
#total_product=len(items)
#print(total_product)

# all_names=[i.get("name") for i in items]
# print(all_names)


# in_stock=[i.get("name") for i in items if i.get("avl_qty")>0]
# print(in_stock)


# price_fiftyfifty=[i.get("name") for i in items if i.get("price") <50]
# print(price_fiftyfifty)

# range_filter=[i.get("name") for i in items if i.get("price") in range(20,50)]
# print(range_filter)

# oreo_price=[ i.get("price") for i in items if i.get("name")=="oreo"]
# print(oreo_price)

# oreo_data=[i for i in items if i.get("name")=="oreo"].pop()
# oreo_data["price"]=90
# print(oreo_data)


# costly_product=max(items,key=lambda d:d.get("price"))
# print(costly_product)


# cheapest_product=min(items,key=lambda d:d.get("price"))
# print(cheapest_product)

# print total number of products!
# print all product names!
# print all in stock product names
# print product names avaialble under rs 50
# print all product names avilable in ranage of 20 to 50