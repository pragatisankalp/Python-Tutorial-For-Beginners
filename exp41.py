class phone :
    _no_buttons=19
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    
    def details(self):
        print(self.color, " ",self.brand)
    
    
    # def text_msg(self):
    #     print("Text msg")
    
    
class Android_phone(phone):
   def __init__(self,color,brand,os):
       super().__init__(color,brand)
       self.os=os

   def extradetails(self):
       super().details()
       print(self.os)
    
    # def audio_msg(self):
    #     print("Text msg")
 
P1=phone('yellow','Nokia')
A1=Android_phone('Blue','Samsung','Android')
A1.details()
print(A1._no_buttons)