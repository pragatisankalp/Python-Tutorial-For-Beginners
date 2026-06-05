                                                                      #Task 8.                                                              
"""Check how many times a given number can be divided by 3 before it is less than
or equal to 10 ."""

num=int(input('Enter your number :'))
count=0
while num>10:
    num=num//3
    count=count+1
    print(num)

print(f"Number is divided {count} times.")
