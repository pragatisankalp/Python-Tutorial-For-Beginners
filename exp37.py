import functools
def decor(func):
    @functools.wraps(func)
    def inner(*arg,**kwarg):
     print('hello guys, welcome to all')
     return func(*arg,**kwarg)
    return inner



@decor
def first(num1,num2):
    '''
     Hello everyone
    '''
    print(f'I am first function and {num1} and {num2}')
    return num1+num2


@decor
def second():
    print('I am second function')

#first=decor(first)
print(first(4,5))


#second=decor(second)
second()
