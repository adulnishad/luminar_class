class Parent:

    phone="iphone12pro"
    bike="access125"
    def mobile(self):
        print(self.phone)
    def vechile(self):
        print(self.bike)


class child(Parent):
    pass


obj=child()
obj.mobile()
obj.vechile()
