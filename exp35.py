class Fruit:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"I am an {self.name}"
    def __repr__(self):
        return f" Fruit : {self.name}"
A1=Fruit("Apple")
print(A1)
print(str(A1))
print(repr(A1))