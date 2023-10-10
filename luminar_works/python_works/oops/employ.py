class Employee:
    id:int
    name:str
    gender:str
    department:str
    salry:int

    def create(self,id,name,gender,department,salry):
        self.id=id
        self.name=name
        self.gender=gender
        self.department=department
        self.salry=salry

    def get(self):
        print(self.id,self.name,self.department,self.salry)
        

emp2=Employee()
emp2.create(1001,"ravi","male","it",50000)
emp1=Employee()
emp1.create(100,"hari","male","hr",900000)
emp1.get()




