    #1. Iteration: """is a process of taking each item of somthing one after another."""
                           #OR
"""Iteration is repetation of process to visit every element from container 
or iterable and consume it"""

#2. Iterable: Iterable is an object, that one can iterate over. Ya jiske upar hum
#iteration perform karte hai.

'''3. Iterator: is an object that allow programmers to traverse through a sequence
of data without storing the data in the memory.'''

#l=[1,2,3,4,5]
'''for x in l:
    print(l)'''

'''def MyOwnLoop(L):
    i=iter(L)
    try:
        while True:
            print(next(i))
    except StopIteration:
        pass

MyOwnLoop(l)
range(2,10)'''

class Even_No:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<10:
            val=self.start
            self.start=self.start+2
            return val
        else:
            raise StopIteration
             
e1=Even_No(2,10)
'''print(next(e1))
print(next(e1))
print(next(e1))
print(next(e1))
print(next(e1))'''

for x in e1:
    print(x)