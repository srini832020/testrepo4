name=["dhoni","kholi","rohit"]
print(name[0][0])
name.insert(1,"dhawan")
print(name)
name.extend(["ashwin","sir"])
print(name)
name.remove("sir")
print(name)
name.pop(3)
print(name)
name.sort()
print(name)
name1=[9,8,27,5]
print(sorted(name1,reverse=True))
var1=[4,3,5,4,7]
for x in var1:
    if x==4:
        var1.remove(x)
print(var1)
var2=[3,5,6,3,7]
if 3 in var2:
    var2.remove(3)
    print(var2)
var3=['dhoni','kohli','ashwin']
var4=[]
for x,y in enumerate(var3):
    z=y[::-1]
    a=z+str(x)
    var4.append(a)
print(var4)
#name.clear
#print(name)
#del name
#print(name)
#var="mohit"
#var[0]='r'
#print(var)



