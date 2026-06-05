# operator overloading
#function pollymorphism
# method overriding
# duck typing
# +
# print(5+6)
# print("Pragati "+ "Gupta")

# print(len("pragati"))
# print(len([1,2,3,4]))

# print(int.__add__(5,6))
# print(str.__add__("pragati","Gupta"))

def fp(a=None,b=None,c=None):
    s=0
    if a!=None and b!=None and c!=None:
        s=a+b+c
    elif a!=None and b!=None:
        s=a+b
    else:
        s=a
    return s
print(fp(3,4,6))
print(fp(8.9,6.7))
print(fp("hello","guys"))