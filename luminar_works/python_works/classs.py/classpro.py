class student:
    def __init__(self,name,course):

        self.name=name
        self.course=course
    def get_student(self):
        print("my name is",self.name,"and my course is",self.course)

obj=student("adhil","python")
obj.get_student()
obj1=student("abc","xyz")
obj1.get_student()


class book:
    def __init__(self): 
        self.id=int(input("enter the id"))
        self.title=input("enter name")
        self.author=input("enter author")
        self.price=int(input("enter price"))

    def getauthor(self):
        print(self.author)
    def gettitle(self):
        print(self.title)
    def setprice(self):
        self.price=int(input("enter price"))
    def settitle(self):
        self.title=input("enter the title")

b1=book()
b1.getauthor()
b1.gettitle()
