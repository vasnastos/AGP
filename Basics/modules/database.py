import sqlite3 as sq
from datetime import date as dt
import temperature as t

class database:
    def __init__(self):
        self.db=sq.connect('modules/temperature.db')
    def Close(self):
        self.db.close()
    def insert(self,temp):
        today=dt.today()
        date=today.strftime("%m/%d/%y")
        sql='insert into temperature(date,temp) values(?,?)'
        self.db.execute(sql,date,temp)
    def getTemperatures(self):
        sql='select * from temperature'
        temperatures=[]
        for x in self.db.execute(sql):
           temperatures.append(t.temperature(x[0],x[1]))
        return temperatures