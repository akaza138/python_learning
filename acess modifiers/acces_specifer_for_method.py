class parent():

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def access_from_same_class(self):
        self.public_method()
        self._protected_method()
        self.__private_method()
class child(parent):
    def access_from_child_class(self):
        self.public_method()
        self._protected_method()
        #self.__private_method() # this will give an error because private method is not accessible from child class
        try:
            self._parent__private_method() # namemangling is used to access the private method from child class
        except AttributeError:
            print("Private method is not accessible from child class")

class another_class():
    def access_from_another_class(self):
        p = parent()
        p.public_method()
        p._protected_method()
        #p.__private_method() # this will give an error because private method is not accessible from another class
        try:
            p._parent__private_method()
        except AttributeError:
            print("Private method is not accessible from another class")

p = parent()
c = child()
a = another_class()
print("Accessing from same class:")
p.access_from_same_class()
print("\nAccessing from child class:")
c.access_from_child_class()
print("\nAccessing from another class:")
a.access_from_another_class()
