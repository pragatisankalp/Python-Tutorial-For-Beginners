# print(len(6))
# # #static typing
# # #dynamic typing

# int X
# X=6
# X="CTC"

# y=8
# print(len(y))
# y="CTC"
# print(len(y))
# y=8.5
# print(len(y))
# #Duck Typing
class duck:
    def quack(self):
        print("It's my sound")

class car:
    def quack(self):
        print("It's my sound too!!")

def func(var1):
    var1.quack()

d1=duck()
c1=car()
func(d1)
func(c1)
a=5
func(a)