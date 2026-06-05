list_1=[1,3]
list_2=[2]

def med(list_1,list_2):
    list_3=list_1+list_2
    list_3.sort()
    if len(list_3)%2!=0:
            median=(len(list_3)/2)
            median=median-0.5
            

print(med(list_1,list_2))
