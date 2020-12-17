def fun2(mylist):
    mylist.append([10,20,30,40])
    print "value inside fn:",mylist
    return
mylist=[1,2,3,4]
fun2(mylist)
print "value outside fn:",mylist
