import sys
var1=('dhoni','kohli','ashwin','dhoni')
print(var1.count('dhoni'))
print(var1.index('dhoni'))
print(sys.getsizeof(var1))
var2=['dhoni','kohli','ashwin','dhoni']
print(sys.getsizeof(var2))
var3={'Name':['Dhoni','Ashwin'],'Age':[37,32]}
print(var3['Name'])
print(var3['Age'])
for x in var3.items():
    print(x)
var3['Name'][1]="Rohit"
print(var3['Name'])
    

