# Module name: datetime
# Class name: datetime,date,time,timedelta,timezone
# The timedelta object has seven arguments: days, seconds, minutes, hours, weeks, milliseconds, and microseconds.
# Birthdate: 4/12/1990
from datetime import date,timedelta
# year=int(input("enter year: "))
# month=int(input("enter month: "))
# day=int(input("enter day: "))
# dob=date(year=year,month=month,day=day)
# #print(dob)
# current_date=date.today()
# #print(current_date)
# diff=current_date-dob
# # print("age is", diff)
# # print(type(diff))
# # 1 year=365.25 days
# age=diff.days//366
# print(age)

current_date=date.today()
print(current_date)
next_date=current_date+timedelta(weeks=4)
print(next_date)