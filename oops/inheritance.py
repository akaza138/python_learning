# to create the parent and child conection
class dad: #parent class
    def house(self):
        print("color : white , size : 2000 sq ft , location : New York")

class son(dad): #child class
    def car(self):
        print("color : black , model : 2020 , location : New York")

s1=son()
s1.house()
s1.car()

# to over write the parent class method in child class
class dad: #parent class
    def house(self):
        print("color : white , size : 2000 sq ft , location : New York")

class son(dad): #child class
    def house(self):
        print("color : black , size : 1500 sq ft , location : New York")
s1=son()
s1.house()  

# to get parent from the differnt file or differen location
class dad: #parent class
    def house(self):
        print("color : white , size : 2000 sq ft , location : New York")
    def car(self):
            print("color : black , model : 2020 , location : New York")
    