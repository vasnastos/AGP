from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import os

class database:
    def __init__(self):
        self.db=QSqlDatabase.addDatabase('QSQLITE')
        QSqlDatabase.setDatabaseName(self.db,'test.db')
        self.db.open()
        print('Database Open')
    def close(self):
        self.db.close()
        print('Database Close')
    def extract(self):
        data='<html><head><style>th{background-color:blue; color:gray;} table{width:80%; background-color:lightgray; color:darkred; font-size:18px; font-weight:bold; text-align:center;}</style><body><center><h1>Database Containts</h1><hr>'
        data+='<table border=\"1\"><tr><th>MODEL</th><th>BRAND</th><th>PRICE</th></tr>'
        sql='select * from car'
        q=QSqlQuery(self.db)
        q.exec_(sql)
        while q.next():
            data+='<tr><td>'+str(q.value(0))+'</td><td>'+str(q.value(1))+'</td><td>'+str(q.value(2))+'</td></tr>'
        data+='</table><br><br></center></body></html>'
        return data
    def insert(self,m,b,p):
        sql='insert into car(model,brand,price) values(?,?,?)'
        q=QSqlQuery(self.db)
        q.prepare(sql)
        q.addBindValue(m)
        q.addBindValue(b)
        q.addBindValue(p)
        q.exec_()


class window(QMainWindow):
    def insertform(self):
        self.model=QLineEdit()
        self.brand=QLineEdit()
        self.price=QDoubleSpinBox()
        self.model.setFixedWidth(0.2*self.width())
        self.brand.setFixedWidth(0.2*self.width())
        self.price.setFixedWidth(0.2*self.width())
        self.brand.setStyleSheet('border:2px solid; color:purple;')
        self.model.setStyleSheet('border:2px solid; color:purple;')
        self.price.setStyleSheet('border:2px solid;')
        self.price.setRange(1000,20000)
        self.but=QPushButton('Add')
        self.but.setStyleSheet('background-color:lightgray; color:blue; font-size:16px;')
        self.but.setFixedWidth(0.2*self.width())
        self.but.clicked.connect(lambda:self.Add())
        self.l1=QHBoxLayout()
        self.l1.addWidget(self.model)
        self.l1.addWidget(self.brand)
        self.l1.addWidget(self.price)
        self.l1.addWidget(self.but)
        self.lay.addLayout(self.l1)

    def __init__(self):
        super().__init__(None)
        self.setWindowTitle('Database Demo')
        self.setFixedSize(300,300)
        self.mydb=database()
        self.mw=QWidget()
        self.lay=QVBoxLayout()
        self.setCentralWidget(self.mw)
        self.mw.setLayout(self.lay)
        self.insertform()
        self.label=QTextEdit()
        self.label.setFixedSize(0.96*self.width(),0.9*self.height())
        self.label.setText(self.mydb.extract())
        self.lay.addWidget(self.label)
    
    def destroy(self):
        self.mydb.close()

    def Add(self):
        self.mydb.insert(self.model.text(),self.brand.text(),self.price.value())
        self.label.setText(self.mydb.extract())

#Main Code
a=QApplication([])
w=window()
w.show()
a.exec()
w.destroy()
