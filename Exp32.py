class Student:
    college_name='IIT'
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
S1=Student("Pragati",12)
#S1.name="Pragati"
#S1.id=12
S2=Student("Neha",13)
Student.college_name='NIIT'
print(Student.college_name)
print(Student.__dict__)
#S1.college_name='NIIT'
print(S1.college_name)
#print(S1.__dict__)
print(S2.college_name)