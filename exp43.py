class phone : 
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    
    def display(self):
        print(f"my color is{self.color}")
   
class Android_phone(): 
    def __init__(self,os):
        self.os=os
        
    def extradetails(self):
        print(f"my operating system is: {self.os}")

class Iphone(phone,Android_phone):
    def func(self):
        super().display()
        super().extradetails()

P1=phone('red','nokia')
A1=Android_phone('window')
I1=Iphone('yellow','samsung')
I1.os='Linux'
I1.func()