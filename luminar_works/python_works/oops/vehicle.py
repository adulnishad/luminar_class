
#------OVERIDING-------

class car:
    def start(self):
        print("key_start")

    def break_type(self):
        print("drum-break")

    def  transmission(self):
        print("manual")

class ambassidor(car):
    pass


class MaruthiEight(car):
    def break_type(self):
        print("disc-break")
    
    def transmission(self):
        print("auto")


obj=ambassidor()
obj.start()


mbj=MaruthiEight()
mbj.break_type()
mbj.transmission()


