class p1:

    def m1(self):
        print("inside class p1 m1 method")

class p2:
    def m2(self):
        print("inside class p2 m2 method")

class Child(p2,p1):
    def m3(self):
        print("inside class Child m3 method")

obj=Child()
obj.m3()
obj.m2()
obj.m1()

