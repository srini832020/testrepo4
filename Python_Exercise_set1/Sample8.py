var=100
if(var==50):
    print "good"
else:
    print "bye"
var1="dhoni"
var2=10
print("my output is %d "%var2)
var3="india is \n my country"
print(var3)
var4=r"c:\next"
print(var4)
print(ord('c'))
print(chr(97))
var5=100.0
print(type(var5))
print(repr(var5))
#print(len(var5))
var6="dhoni msd"
count=0
for x,y in enumerate(var6):
    count+=1
    if x==4 or count==5:
        print("done",count)
        break
    else:
        print("no",count)
var7=10
var8=20
print(var7,var8)
del var7,var8
print(var7,var8)


