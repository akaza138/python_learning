# the static method run independently and does not depend on the object or the class
# it just run what it need to run

class math():
    @staticmethod
    def add(x,y):
        return x+y
print(math.add(12,788))