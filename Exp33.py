"""books=['Python','Java','C++']
print(books.__class__)
print(len(books))
print(list.__len__(books))"""
class Library:
    def __init__(self):
        self.subjects=[]
    def __len__(self):
        return len(self.subjects)
    def __getitem__(self,i):
        return self.subjects[i] 
    
b1=Library()

b1.subjects.append('Python')
b1.subjects.append('java')
b1.subjects.append('C++')
print(b1)
print(b1.subjects)
print(len(b1))
print(b1[1])
print(Library.__getitem__(b1,1))
for x in b1:
    print(x)
