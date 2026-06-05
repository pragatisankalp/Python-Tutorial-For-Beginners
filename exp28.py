#def avg(seq):
    #return sum(seq)/len(seq)
"""avg=lambda seq: sum(seq)/len(seq)
total=lambda seq:sum(seq)
top=lambda seq:max(seq)"""

operations={"avg":lambda seq: sum(seq)/len(seq),
            "total":sum,
            "max":max}

students=[{"name":"Parul","mark":(67,98,45,56)},
                     {"name":"Priya","mark":(77,95,35,46)},
                     {"name":"Rayensh","mark":(97,98,55,66)},
                     {"name":"Nisha","mark":(69,89,45,57)},
           ]
for student in students:
    name=student["name"]
    marks=student["mark"]
    print(f"student name is {name}")
    
    operation=input("Enter your operation:")
    opertion_function=operations[operation]
    print(opertion_function(marks))
    
    

    
 


