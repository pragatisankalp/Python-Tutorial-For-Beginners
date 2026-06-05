class Student:
    college_name="IIT"
    def __init__(self,name,id):
        self.id=id
        self.name=name
        
S1=Student('Pragati',123)
"""S1.name='Pragati'
S1.id=123"""
S2=Student('Shreya',456)
"""S2.name='Shreya'
S2.id=456"""

Student.college_name='NIT'
S1.college_name='AKTU'
print(S1.college_name)
print(S1.__dict__)
print(S2.college_name)
print(S2.__dict__)
print(Student.college_name)