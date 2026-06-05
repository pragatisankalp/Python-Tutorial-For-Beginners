# # timezone
# """time zone represents the standardized time depending on which 
# part of the world is being considered.
# """
from datetime import datetime,timezone
import pytz
#naive object
print(datetime.now())
#aware object
print(datetime.now(timezone.utc))
# count=0
# for x in pytz.all_timezones:
#     count=count+1
#     print(x)
# print("total no of timezones:  ",count)    

for y in pytz.country_timezones['IN']:
    print(y)

date_new=datetime.now(pytz.timezone('Asia/Kolkata'))
print(date_new)
print("formatted date: ",date_new.strftime('%y:%m:%d %H:%m:%s %Z '))