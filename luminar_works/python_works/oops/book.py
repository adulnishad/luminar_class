
class book:
    book_name:str
    author:str
    price:int
    pages:int


    def __init__(self,book_name,author,price,pages):

        self.book_name=book_name
        self.author=author
        self.price=price
        self.pages=pages
        # initilazing instance variable constructor

    def get(self):
        print(self.book_name,self.author)

    def __str__(self):
        return self.book_name+str(self.price)    

obj=book("got","tary",580,908)

print(obj)





