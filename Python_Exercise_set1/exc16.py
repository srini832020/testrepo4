'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class cname:
    def __init__(Self,Color,Model):
        Self.Color=Color
        Self.Model=Model
    def car(Self):
        print(Self.Color)
class cname2(cname):
    def __init__(Self,Color,Model):
        cname.__init__(Self,Color,Model)
        Self.Color1=Color
        Self.Model1=Model
    def bike(Self):
        print(Self.Model)
obj=cname2('red','r10')
obj.car()
obj.bike()
#Class Composition
    
      
