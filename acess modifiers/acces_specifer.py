'''
in the acess specifire concept there are 3 types of access specifier in python
1. public access specifier
2. protected access specifier
3. private access specifier

SYNTAX:
1.public access specifier: simply the variable or method name without any underscore
2.protected access specifier: the variable or method name with single underscore
3.private access specifier: the variable or method name with double underscore'''

class parent():
    def __init__(self):
        self.public_variable = "This is a public variable"
        self._protected_variable = "This is a protected variable"
        self.__private_variable = "This is a private variable"
    def acess_from_same_class(self):
        print(self.public_variable)
        print(self._protected_variable)
        print(self.__private_variable) 
class child(parent):
    def acess_from_child_class(self):
        print(self.public_variable)
        print(self._protected_variable)
        #print(self.__private_variable) # this will give an error because private variable is not accessible from child class
        try:
            print(self._parent__private_variable) # namemangling is used to access the private variable from child class
        except AttributeError:
            print("Private variable is not accessible from child class")
class another_class():
    def acess_from_another_class(self):
        p = parent()
        print(p.public_variable)
        print(p._protected_variable)
        #print(p.__private_variable) # this will give an error because private variable is not accessible from another class
        try:
            print(p.__private_variable)
        except AttributeError:
            print("Private variable is not accessible from another class")
p = parent()
c = child()
a = another_class()
print("Accessing from same class:")
p.acess_from_same_class()
print("\nAccessing from child class:")
c.acess_from_child_class()
print("\nAccessing from another class:")
a.acess_from_another_class()
