class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def great(self):
        print(f"Hello {self.name}, welcome to the student class and your age is {self.age}! ")

s1 = student("vishal",21)
s2= student("John",30)
s3=student("Alice",25)
s1.great()
s2.great()
s3.great()