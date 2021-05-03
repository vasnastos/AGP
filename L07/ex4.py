from bs4 import BeautifulSoup as bs
import pandas as pd
import sqlite3 as sq
import pip._vendor.requests as req



class database:
    def __init__(self):
        self.db=sq.connect('teachers.db')
        self.c=self.db.cursor()
        self.c.execute('create table if not exists teacher(name text,position text,mailphone text,primary key(name))')

    def Close(self):
        self.db.close()
    
    def Insert(self,name,pos,info):
        self.c.execute('insert into teacher(name,position,mail-phone) values(?,?,?)',(name,pos,info))

    def scrap(self):
        data=req.get('https://www.dit.uoi.gr/members.php')
        soup=bs(data.text,features="lxml")
        for x in soup.findAll('table'):
            for y in x.findAll('tr'):
                td=y.findAll('td')
                if len(td)<3:
                    print('Not an acceptable record')
                    continue
                self.Insert(td[0],td[1],td[2])
    

    def extract(self):
        members=self.c.execute('select * from teacher')
        df=pd.DataFrame(members,columns=['Name','Position','Info'])
        print(df)


db=database()
db.scrap()
db.extract()
db.Close()