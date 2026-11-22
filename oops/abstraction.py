from abc import ABC,abstractmethod # library

class feature(ABC):
    @abstractmethod
    def fe1(self):
        pass

    @abstractmethod
    def fe2(self):
        print("this is the feature 2")
        pass
     
    def fe3(self):
        pass

class fe1(feature):
    def fe1(self):
        print("this is the feature 1")

    def fe2(self):
        print("this is the feature 2 and modified in the child class")


f = fe1()
f.fe1()
f.fe2()
f.fe3()