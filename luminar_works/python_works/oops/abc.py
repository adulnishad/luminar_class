from abc import ABC

class Bike(ABC):

    def start(self):
        pass
    def breaks(self):
        pass
    def acclerate(self):
        pass


class Hunter(Bike):
    pass

obj=Hunter()
obj.start()