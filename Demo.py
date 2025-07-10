class Demo:
    def Show(self,a=None,b=None,c=None):
        if a and b and c:
            print("3 args")
        elif (a and b) or (a and c) or (b and c):
            print("2 args")
        elif b or c or a:
            print("1 args")
        else:
            print("no args")
d=Demo()
d.Show(0,5,4)
d.Show()