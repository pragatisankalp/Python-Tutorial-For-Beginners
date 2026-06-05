class A:
    def m1(self):
        print("In class A")
class B(A):
    # def m1(self):
    #     print("In class B")
    pass
class C(A):
    # def m1(self):
    #     print("In class C")
    pass
class D(B,C):
    pass
d1=D()
d1.m1()
print(D.mro())