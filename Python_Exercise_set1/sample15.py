import time;
print "Hello Python"
if True:
    print"Answer yes"
else:
    print"Answer no"
    #first comment
print "Hi Srini"#second Comment
print"-------------------------------------"
var1=10
var2=20.0
var3="Jaya"
print var1
print var2
print var3
a=b=c=1
print a,b,c
d,e,f=1,2,"John"
print d,e,f
print"--------------------------------------"
str="hello world"
print str
print str[0]
print str[2:5]
print str + "test"
print"--------------------------------------"
list1=["abc",1,"cde",2,"fgh",3]
list2=["klm",2]
print list1
print list1[0]
print list1[1:3]
print list2
print list1+list2
print"--------------------------------------"
tuple1=("abc",1,"cde",2,"fgh",3)
tuple2=("klm",2)
print tuple1
print tuple1[0]
print tuple1[1:3]
print tuple2
print tuple1+tuple2
print"--------------------------------------"
dict={}
dict['one']="this is one"
tinydict={'name1':'suresh','age1':10,'dept1':'IT','name2':'kamesh','age2':20,'dept2':'CSE'}
print dict
print dict['one']
print tinydict
print tinydict['name2']
print tinydict.keys()
print tinydict.values()
print"--------------------------------------"
var6=100
if(var6==100):
   print "Good bye"
print"--------------------------------------"
def fun():
    return;
print("First Call")
print("Second Call")
print "this is good time to learn"
print"--------------------------------------"
def fun1(mylist):
    mylist.append([1,2,3,4]);
    print "values inside the function:",mylist
    return
mylist=[6,7,8]
fun1(mylist)
print "values outside the function",mylist
print"--------------------------------------"
def fun2(mylist1):
    mylist1=[1,2,3,4];
    print "values inside the function:",mylist1
    return
mylist1=[6,7,8]
fun2(mylist1)
print "values outside the function",mylist1
print"--------------------------------------"
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;
printinfo( age=50, name="miki" )
print"--------------------------------------"
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;
# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
print"--------------------------------------"
ticks=time.time();
print ticks
