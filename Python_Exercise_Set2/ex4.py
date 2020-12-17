print "List Manipulation"
list1=['physics','chemistry',1997,2000,2000,1997]
list2=[1,2,3,4,5,6,7]
print "list1 is:" ,list1[0]
print "list2 is:", list2[1:5]
print "old list1 is:",list1
list1[3]=2001
print "new list is:",list1
del list1[2]
print "new list is:",list1
print len(list1)
print "End List"
#################################
print "String Manipulation"
str="hello srini"
print str
print str[0]
print str[1:3]
print len(str)
print "End"
###################################
print "tuple manipulation"
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
####################################
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print len(tup3)
print "end"
####################################
print "dict manipulation"
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict['Name']
dict['Age']=8
dict['School']='DPS School'
print dict
del dict['School']
print dict.keys()
print dict.values()
print "end"
######################################
