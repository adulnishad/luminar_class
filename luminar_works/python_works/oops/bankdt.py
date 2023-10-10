class Bank:
    accno:str
    name:str
    ifsccode:str
    branch:str
    ac_type:str
    balance:int


    def create(self,accno,name,ifsccode,branch,ac_type,balance):
        self.accno=accno
        self.name=name
        self.ifsccode=ifsccode
        self.branch=branch
        self.ac_type=ac_type
        self.balance=balance


