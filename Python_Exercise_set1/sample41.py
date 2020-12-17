import time
var=open("new.txt",'r')
var1=(var.readlines())
var2=[]
#y=0
for x in var1:
    time.sleep(2)
    y=time.ctime()
    y=y.replace(":","_")
    x=x.strip('\n')
    x=x+ y + '.txt'
    #x=x+str(y)+.'txt'
    a=open(x,'w')
    a.write('yes')
#   var2.append(x)
#print(var.readline())
#var.write("hello world")
#var.write("world is big")
#print var2
var.close()
a.close()
