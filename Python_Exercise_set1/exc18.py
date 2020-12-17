'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from abc import ABC, abstractmethod

class power(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def ninja(self):
        pass
##        print("galaxy force")
        

class rangers(power):
    def timeforce(self):
        print("dino thunder")      ## function overloading, instance , protected is not available in python
    def ninja():
        pass
pr=rangers()
pr.timeforce()

