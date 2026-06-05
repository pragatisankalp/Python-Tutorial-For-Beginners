a=int(input('a:'))
try:
    b=int(input('b:'))  
    if b==0:
        raise ValueError('enter correct value1') 
    c=a/b
    print(c)
except ZeroDivisionError:
   print("can't divide from zero")
except ValueError as e:
    print('enter correct value',e)
except Exception as e:
    print(e)
else:
    print("code is successfully completed")
finally:
    print('exit')