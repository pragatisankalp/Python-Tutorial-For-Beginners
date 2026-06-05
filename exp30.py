"""student_data={'name':'Riya','marks':[98,97,65,87]}
def avg_marks(student):
    return sum(student['marks'])/len(student['marks'])"""

class Student:
    def __init__(self,name,marks):  
        self.f_name=name
        self.S_marks=marks

    def avg_marks(self):
        return sum(self.S_marks)/len(self.S_marks)

S1=Student("Pragati",[88,79,56,45])
S2=Student("Neha",[65,78,98,100])
print(S1.avg_marks())
#print(Student.avg_marks(S1))
