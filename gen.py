#Generators are iterators.
#It returns object using Yield keyword that produce value at a time.

def Even_No(num):
   while num<10:
      yield num
      num=num+2
 
e=Even_No(2)
print(next(e))
for x in e:
   print(x)