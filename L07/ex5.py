import datetime as dt
from time import time

print(dt.datetime.now())
print(dt.datetime(2020,4,29))
print(dt.datetime.today().strftime('%y/%m/%d %H:%M:%S'))
print(dt.datetime.fromtimestamp(time()))
print(dt.datetime.today())