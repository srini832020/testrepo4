class name1:
    def fun(self):
        print("yes")
class name2(name1):
    def __fun(self):
        print("no")
g1=name1()
g2=name2()
g1.fun()
g2.__fun()

