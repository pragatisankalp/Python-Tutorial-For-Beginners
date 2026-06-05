'''Given a list of numbers, identify the perfect squares , 
add 2 to each of these perfect squares, 
and then find the multiplication of the resulting values.''' 
from functools import reduce
num=[4,5,5.8,12,16,15,7.5,25,1,2.8,9.7]
'''
#1. Using for loop

perfect_square=[]
for x in num:
    if x==int(x**.5)**2:
        perfect_square.append(x)
print(perfect_square)

#2. List Comprehension

perfect_square=[x for x in num if x==int(x**.5)**2]
print(perfect_square)

#3. Using filter()

def is_perfect_square(x):
    return x==int(x**.5)**2

x=list(filter(is_perfect_square,num))
print(x)
#print(next(x))
#print(next(x))'''

#4. Using Lambda()
#perfect_square=list(filter(lambda x: x==int(x**.5)**2,num ))
#print(perfect_square) #   [4, 16, 25, 1]

# 2nd Task using map()
'''def add(x):
    return x+2

updated_list=list(map(add,perfect_square))
#print(next(updated_list),end=" ")
#print(next(updated_list),end=" ")
print(updated_list)'''

#updated_list=list(map(lambda x: x+2,perfect_square))
#print((updated_list)) # [6, 18, 27, 3]

# 3rd Task

'''def final_task(a,b):
    return a*b

final_value=reduce(final_task,updated_list)
print(final_value)'''

perfect_square=list(filter(lambda x: x==int(x**.5)**2,num ))

updated_list=list(map(lambda x: x+2,perfect_square))

final_value=reduce(lambda a,b: a*b,updated_list)
print(final_value)