class Student:
    college_name='IIT'
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def Total_marks(self):
        return sum(self.marks)
    @staticmethod
    def play_games(game):
        print(game)

    @classmethod
    def update_college_name(cls,new_name):
        cls.college_name=new_name
        return cls.college_name
    
    
S1=Student("Pragati",[12,13,15])
#print(S1.Total_marks())
#print(Student.Total_marks(S1))
#Student.college_name="NIIT"
print(Student.update_college_name('NIIT'))
print(S1.update_college_name('NIIT'))
S1.play_games("Cricket")
Student.play_games("Cricket")