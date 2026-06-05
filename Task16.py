'''
======================
    Hello everyone
======================
'''
def decor(func):
    def inner():
        print('*'*20)
        func()
        print('='*20)
    return inner
@decor
def test():
    print("Hello everyone")

test()