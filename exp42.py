class phone : 
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    
    def display(self):
        print(f"my color is{self.color}")
   
class Android_phone(phone): 
    def __init__(self,color,brand,os):
        #phone.__init__(self,color,brand)
        super().__init__(color,brand)
        self.os=os
    def extradetail(self):
        super().display()

P1=phone('red','nokia')
A1=Android_phone('Yellow','samsung','window')
print(A1.os)
A1.extradetail()