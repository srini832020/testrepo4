##class cname:
##    def __fun(va):
##        print("dhoni scored ",va)
##    __fun(40)
##
##cname


##class name:
##    def fun():
##        print("yes")
##class name2(name):
##    def __fun():
##        print("no")
##name2.fun()

##class a:
##    def fun():
##        print("a")
##class b(a):
##    def fun():
##        print("b")
##class c(a):
##    def fun():
##        print("c")
##class d(b,c):
##    pass
####    def fun():
####        print("d")
##d.fun()

class cname:
    """this is nothing"""
    def fun():
        print("yes")
cname.fun()
print(cname.__doc__)
"""unbound methond: calling evey time with function names"""

class cc:
    def fun(var):
        print(var)
class gg:
    def fun(var1):
        print(var1)
cc.fun("shadow")
gg.fun("fiend")






