#import array 
#array=array()
#import array as arr
#arr.array()
from array import *
# i type code for iigned integer
# we can't add float value like 8.9 it give error
# we can add -ve value
vals=array('i',[7,5,3,-1])
# val_1=array('u',['a','e','i'])
# print(val_1)
# print(vals.buffer_info()) # return address and size of array
# vals.reverse()
# print(vals)
# print(vals[0])
# for i in range(len(vals)):
#     print(vals[i])

# creating a new array of square of vals array
new_arr=array(vals.typecode,(a*a for a in vals))
for i in new_arr:
    print(i)


