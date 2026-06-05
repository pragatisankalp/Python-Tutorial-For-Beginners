'''In some cases, you want the decorator itself (rather than the decorated function) to accept arguments.

To create a decorator that accepts arguments, you need to create a 'meta-decorator' function that takes arguments and returns a regular decorator, which in turns returns a function. So there are three layers of functions!

To create a decorator that can accept arguments, but also works without, you have to inspect whether the first argument to the decorator is a callable (e.g. a function); if so, then act as regular decorator; if not, then act as a meta-decorator.

All of this sounds more complicated then it is. Let's take a look.'''

import functools
def outer(times):
    def decor(func):
        @functools.wraps(func)
        def inner(*arg,**kwarg):
            for x in range(times):
                func(*arg,**kwarg)
            return func(*arg,**kwarg)
        return inner
    return decor


#@outer(5)
def first(num1,num2):
    
    print(f'I am first function and {num1} and {num2}')
    


@outer(10)
def second():
    print('I am second function')

#first=decor(first)
#first(4,5)
outer(5)(first)(4,5)


#second=decor(second)
second()
