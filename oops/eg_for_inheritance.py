
# to get parent from the differnt file or differen location
from inheritance import dad
# multilevel inheritance
class son(dad):
    print("This is the child class")
    def house(self):
        print("color : black , size : 1500 sq ft , location : New York and this is the child class method")

s1=son()
s1.house()
s1.car()

class cousin(son):
    def new_property(self):
        print("This is the cousin class and this is the new property method")   
s2=cousin()
s2.new_property()
s2.house()
s2.car()


# mulptiple inheritance
class dad:
     def house(self):
         print("it is the dad's house")
class mom:
    def car(self):
        print("it is the mom's car")

class daughter(dad,mom):
    def bike(self):
        print("it is the daughter's bike")

    def car(self):
            print("now it became my car")

    def house(self):
             print("now it became my house")
s=daughter()
s.house()
s.car()
s.bike()

#hybrid inheritance

# Parent class
class Father:
    def father_property(self):
        print("Father: Owns a house")


# Another parent class
class Mother:
    def mother_property(self):
        print("Mother: Owns a car")


# Single inheritance: Son inherits from Father
class Son(Father):
    def son_property(self):
        print("Son: Owns a bike")


# Multiple inheritance: Daughter inherits from Son and Mother
class Daughter(Son, Mother):
    def daughter_property(self):
        print("Daughter: Owns a laptop")


# Creating an object
d = Daughter()

# Calling inherited and own methods
d.father_property()
d.mother_property()
d.son_property()
d.daughter_property()
