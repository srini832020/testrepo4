class a:
    def fun():
        print("a")
class b(a):
    def fun():
        print("b")
class c(a):
    def fun():
        print("c")
class d(b,c):
    def fun():
        print("d")
c=d
d.fun()

