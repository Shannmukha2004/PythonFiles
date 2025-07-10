class Account:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.__blnc = 0
    def getBlnc(self):
        return self.__blnc
    def setBlnc(self,blnc):
        self.__blnc += blnc
acc=Account("abc",20)
print(acc.getBlnc())
acc.setBlnc(10000)
print(acc.getBlnc())
ac2=Account("abc",12)
print(ac2.getBlnc())
ac2.setBlnc(10000)
print(ac2.getBlnc())