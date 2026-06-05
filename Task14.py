"""Create a Emarket class,It has name and list of items.
In this exercies, we will let you design architecture and inner methods of the Emarket class.
And your goal is to implement the proper methods so that other can intract with this class as 
follows:
1.You should able to create an instance of Emarket class.
2.You should be able to add items to the object.
3.You should be able to access the i-th item (assuming i-th item is always valid)
4.At last,you will need to define two methods that do the following work:

    a)One of the should return a readble string to the user about object. The return value should
    look like this: Emarket have 3 items.
    
    b) The other should return a string representation of the current object so that it can be 
    used by others to recreate this object.The return value should look like this:
    Emarket Emarket_name :['Electronics','Groceries','Plats']
    
"""
class Emarket:
    def __init__(self,name):
        self.name=name
        self.items=[]
    def __getitem__(self,i):
        return self.items[i] 
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return f"Emarket have {len(self)} items"
    def __repr__(self):
        return f"{self.name} :['Electronics','Groceries','Plats']"

E1=Emarket("CTC")
E1.items.append('Electronics')
E1.items.append('Plants')
E1.items.append('Groceries')
print(E1.items)
print(E1[0])
"""for x in E1:
    print(x)"""
print(E1)
print(repr(E1))