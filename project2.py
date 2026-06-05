class InvalidPrice(Exception):
    pass
class WrongCard(Exception):
    pass
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no=card_no
        self.balance=balance
class Customer:
    def __init__(self) :
        self.cards={}
    
    def purchase_item(self,card_no,price):
                try:
                    if price < 0:
                        raise InvalidPrice("The price is wrong")
                    if card_no not in self.cards:
                        raise WrongCard("Card is invalid")
                    if price>self.cards[card_no]:
                        raise WrongCard("Card has insufficient balance")
                except InvalidPrice as e:
                    print(e)
                except WrongCard as e:
                    print(e)       
                except Exception as e:
                    print("Something went wrong. ")
                else:
                    print('code is successfully ')
card1=CreditCard(101,5000)
card2=CreditCard(102,2000)
l=[card1,card2]
c=Customer()
for x in l:
    if x not in c.cards:
        c.cards[x.card_no]=x.balance
cardno=int(input("cardno: "))
price=int(input("price: "))
