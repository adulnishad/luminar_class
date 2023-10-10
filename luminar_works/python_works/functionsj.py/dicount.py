def get_discount_price(acutal_price,discount):
    selling_price=(100)/(100+discount)*acutal_price
    return selling_price
print(get_discount_price(50,10))