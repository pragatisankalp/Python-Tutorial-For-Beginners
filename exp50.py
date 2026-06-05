class ValueToosmall(Exception):
    pass
class ValueToolarge(Exception):
    pass
a=int(input('a:'))
try:
    b=int(input('b:'))
    if b<0:
        raise ValueToosmall(b)
    if b==0:
        raise ArithmeticError(b)
    if b>1000:
        raise ValueToolarge(b)
    c=a/b
    print(c)
except ArithmeticError as e:
    print(e)
except ValueToolarge as e:
    print("Value of b should be less than 1000",e)
except ValueToosmall as e:
    print("don't enter -ve value",e)
except Exception as e:
    print(e)