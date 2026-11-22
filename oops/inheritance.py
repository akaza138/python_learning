''''
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

'''

class dad: #parent class
    def house(self):
        print("color : white , size : 2000 sq ft , location : New York")

    def land(self):
        print("parent has land")

class son(dad): #child class
    def car(self):
        print("color : black , model : 2020 , location : New York")
    def bike(self):
        print("color : white , size : 1500 sq ft , location : New York")
    def house(self):
        print("color : white , size :  1500 sq ft , location : New York")

obj=son()
obj.car()
obj.house()
obj.land()








class mom:# parent
    def house(self):
        print("mom got house")
    def mobile(self):
        print("mom got mobile")

class child(mom):#child
    def bike(self):
        print("child got bike")
    def car(self):
        print("child got car")

obj=child()
obj.bike()
obj.house()
obj.car()
obj.mobile()

#multiple inheritance
class mom:# parent
    def house(self):
        print("mom got house")
    def mobile(self):
        print("mom got mobile")

class dad:# parent
    def car(self):
        print("mom got house")
    def land(self):
        print("mom got mobile")

class son(mom,dad):
    def bike(self):
        print("i got bike")
    
    '''
#multilevel inheritance

class thatha:# parent
    def car(self):
        print("mom got house")
    def land(self):
        print("mom got mobile")

class dad(thatha):# chid # parent
    def car(self):
        print("mom got house")
    def land(self):
        print("mom got mobile")

class son(dad):# child
    def bike(self):
        print("i got bike")



# heiarchical inheritance

class dad:
    def eat(self):
        print("Eating")

class son1(dad):
    pass

class son2(dad):
    pass

Dog().eat()
Cat().eat()

