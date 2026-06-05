 #                               Chapter 1
from abc import ABCMeta, abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def Return_policy(self):
         pass
    def display(self):
        print("I am normal method")
    
class Mobile(Product):
    def Return_policy(self):
         print("All products must be returned within 10 days ")

class Computer(Product):
    # def Return_policy(self):
    #      print("All products must be returned within 15 days ")
    pass
   
class Book(Computer):
    pass
#P1=Product()
M1=Mobile()
M1.Return_policy()
M1.display()
C1=Computer()
C1.Return_policy()
B1=Book()
B1.Return_policy()