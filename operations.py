# def sub(x,y):
# 	return x-y

# def greet():
# 	print("Hello everyone")
# if __name__=="__main__":
# 	greet()


# class Ex(Exception):
#     def __init__(self,msg):
#         Exception.__init__(self,msg + msg)
#         self.args(msg,)


# class A:
#     def __init__(self,v=2) :
#         self.v=v
#     def set(self,v=1):
#         self.v+=v
#         return self.v
# a=A()
# b=a
# b.set()
# print(a.v)

# def o(p):
#     def q():
#         return '*' * p
#     return q

# r=o(1)
# s=o(2)
# print(r()+s())


# x="\"
# print(len(x))

# from datetime import datetime
# dt1=datetime(2019,11,27,11,27,22)
# dt2=datetime(2019,11,27,0,0,0)
# print(dt1-dt2)

# print(chr(ord('p')+2))

# num=[i*i for i in range(5)]
# foo=(filter(lambda x: x%2,num))
# print(foo())


# class A:
#     A=1
#     def __init__(self):
#         self.a=0

# print(hasattr(A,'A'))


# t=[1,2,3,4]
# t=t[-2:-1]
# t=t[-1]
# print(t)
# class X:
#     pass

# class Y(X):
#     pass

# class Z(Y):
#     pass
# x=X()
# z=Z()

# print(isinstance(x,Z), isinstance(z,X))

# d={}
# d['2']=[1,2]
# d['1']=[3,4]

# for x in d.keys():
#     print(d[x][1])
# l=[1,2,3,4]
# l=list(map(lambda x:2*x,l))
# print(l)


print(len([i for i in range(0,-2)]))