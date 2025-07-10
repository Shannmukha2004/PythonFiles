class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        print(self.name)

    def getage(self):
        print(self.age)
s1=Student("Ashish",22)
s1.getname()
s1.getage()
s2=Student("Ashi",20)
s2.getname()
s2.getage()
