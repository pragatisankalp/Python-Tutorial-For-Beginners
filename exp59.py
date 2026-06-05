# Time Module
# 1 epoch= is the time where the time starts. It is January 1, 1970, 00:00:00 (UTC) 
# on all platforms.
import time
start_time=time.time()
# print(f"start time is: {start_time} ")
l=[11,31,21,45,65]
for x in l:
    time.sleep(1*60)
#     print(x)
end_time=time.time()
# print(f"end time is: {end_time} ")
# z=end_time-start_time
# print(z)
# print(f"{z:f}")
print(time.ctime())