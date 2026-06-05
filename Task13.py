"""
Create a class Employee that keeps a track of the number of employees in the organization,total no of leaves of employees and also store their name,designation and salary details.

Create a method named display_count which print the Total no of employees in the organization.

Create a method named display_details which print the Employee's informations(name,desiganation,salary,no_of leaves)
""" 
class Employee:
    no_of_emp=0
    no_of_leaves=17
    def __init__(self,name,desi,salary):
        self.name=name
        self.desi=desi
        self.salary=salary    
        Employee.no_of_emp=Employee.no_of_emp+1
    def display_count(self):
        print(f"Total no of employee is{Employee.no_of_emp}") 
    def display_details(self):
        print(self.name ," ",self.desi," ",self.salary," ",self.no_of_leaves)
E1=Employee('Pragati','Programmer',1000)
E2=Employee('Priya','Programmer2',2000)        
E3=Employee('Rahul','Programmer3',3000)
E1.display_count()
#Employee.display_count(E1)
E2.display_details()
