class Wrong_card_error(Exception):
    pass
class Invalid_price_error(Exception):
    pass
class Creditcard:
    def __init__(self,cardno,balance):
        self.cardno=cardno
        self.balance=balance
class Customer:
    def __init__(self):
        self.cards={}
    def purchase_item(self,cardno,price):
        if cardno not in self.cards:
            raise Wrong_card_error("card is invalid ")
        if price<0:
            raise Invalid_price_error("Price is wrong")
        if price>self.cards[cardno]:
            raise Invalid_price_error("card has insufficient balance")
        
card1=Creditcard(101,25000)
card2=Creditcard(102,50000)
c=Customer()
l=[card1,card2]
for x in l:
    if x not in c.cards:
        c.cards[x.cardno]=x.balance
while(True):
    cardno=int(input("enter your card no: "))
    try:
        price=int(input("enter the price: "))
        c.purchase_item(cardno,price)        
    except Invalid_price_error as e:
        print(e)
        break
    except Wrong_card_error as e:
        print(e)
        continue
    except Exception as e:
        print("Something went wrong",e)
        break
    else:
        print("items are purchased sucessfully")  
        break
