#public
#private
#protected

class Customer:
   
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self._name = name
        self.age = age
        self.__wallet_balance = wallet_balance
        #self._Customer__wallet_balance=wallet_balance
        
        
    def __update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount 
        
    def _show_balance(self): 
        c1.__update_balance(500) 
        print(self.__wallet_balance)
           
c1=Customer(100, "Gopal", 24, 1000)
c1.__wallet_balance=5000
#c1.__update_balance(500)
c1._show_balance()
#print(c1.__wallet_balance)
#print(c1._Customer__wallet_balance)
print(c1._name)
