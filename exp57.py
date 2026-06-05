# Module name: datetime
# Class name: datetime,date,time,timedelta,timezone
from datetime import datetime
cur_date=datetime.now().time()
# print(cur_date)
from datetime import date
cur_date=date.today()
# print(cur_date)
# print("year is: ",cur_date.year)
# print("month is: ",cur_date.month)
# print("Day is: ",cur_date.day)
print(type(cur_date))
y=date.isoformat(cur_date)
# print(type(y))
# #strftime()
change_date=cur_date.strftime("%d-%m-%y")
# print(change_date)
# my_date=date('2025',12,30)
# print(my_date)
# from datetime import datetime
from datetime import time
# cur_date=datetime.now().time()
# print(cur_date)
# print("Hour is: ", cur_date.hour)
# print("min is: ", cur_date.minute)
# print("sec is: ", cur_date.second)
t1=time(13,45,56)
print(t1)
t2=time()
print(t2)
t3=time(minute=45)
print(t3)