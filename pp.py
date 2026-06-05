class Even_num:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.stop:
            #val=self.start
            self.start=self.start+2
            return self.start
        else:
            raise StopIteration
e1=Even_num(2,10)
for x in e1:
    print(x,end=" ")