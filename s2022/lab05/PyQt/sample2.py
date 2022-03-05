from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
import mysql.connector as cnt


class Movie:
    def __init__(self,mid,mname,mrelease,mimdb):
        self.id=mid
        self.name=mname
        self.release_date=mrelease
        self.imdb=mimdb


class Database:
    @staticmethod
    def establish_connection():
        return cnt.connect(
            host='myweb.dit.uoi.gr',
            database='movielen',
            user='agproot',
            password='!Ditagp2022'
        )
    def __init__(self):
        self.connector=None
    
    def set_connector(self,db_connector):
        self.connector=db_connector

    def description(self):
        self.connector=Database.establish_connection()
        cursor=self.connector.cursor()
        query="SELECT id,name,release_date,imdb FROM movie"
        cursor.execute(query)
        return cursor.description
    
    def get_records(self):
        self.connector=Database.establish_connection()
        cursor=self.connector.cursor()
        query="SELECT id,name,release_date,imdb FROM movie"
        cursor.execute(query)
        return [Movie(row[0],row[1],row[2],row[3]) for row in cursor.fetchall()]


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(600,600)
        self.setWindowTitle("Table View")
        self.db_instance=Database()
        self.table_name='movie'
        w=QWidget()
        w.setFixedSize(self.width(),self.height())
        self.setCentralWidget(w)
        self.layout_manager=QVBoxLayout()
        w.setLayout(self.lay)

        self.view=QTableWidget(self)
        self.view.setVisible(False)
        self.layout_manager.addWidget(self.view)
    
    def SqlTable(self):
        self.view.setToolTip('Movie Len DB')
        records=self.db_instance.get_records()

        self.view.setRowCount()

    def panel1(self):
        w1=QWidget()
        w1.setFixedSize(0.45*self.width(),0.3*self.height())
        lay1=QVBoxLayout()
        w1.setLayout(lay1)
        b1=QPushButton(self)
        b1.setFixedWidth(0.3 * self.width())
        b1.setText("CONNECT")
        b1.setStyleSheet(
            """
            QPushButton{
                color:white;
                font-weight:bold;
                font-size:16px;
                background-color:#353f9c;
            }
            OPushButton:hover
            {
                color:#353f9c;
                background-color:white;
                font-weight:italics;
            }
            """
        )
        b1.clicked.connect(self.connect_action)
        self.panel1()
        self.layout_manager.addWidget(b1)

    def connect_action(self):
        w=QMainWindow()
        w.setFixedSize(200,200)
        central_widget=QWidget()
        central_widget.setFixedSize(w.width(),w.heihgt())
        w.setAutoFillBackground(True)
        lay=QVBoxLayout()
        w.setLayout(lay)
        label1=QLabel()
        l1=QLineEdit()
        label2=QLabel()
        l2=QLineEdit()
        l2.setEchoMode(QLineEdit.Password)
        label1.setFixedSize(0.3*w.width(),0.12*w.height())
        l1.setFixedSize(0.3*self.width())
        label2.setFixedSize(0.3*w.width(),0.12*w.height())
        l2.setFixedSize(0.3*self.width())
        
        b1=QPushButton()
        b2=QPushButton()
        b1.setText("SUBMIT")
        b2.setText("CLEAR")
        b1.setFixedWidth(0.15*w.width())
        b2.setFixedWidth(0.15*w.width())

        b1.setStyleSheet(
            """
            QPushButton{
                color:white;
                background-color:#33568f;
                font-size:bold;
            }
            """
        )
        b2.setStyleSheet(
            """
            QPushButton{
                color:white;
                background-color:#33568f;
                font-size:bold;
                bold:3px solid red;
            }
            """
        )

        b1.clicked.connect(connection_action)
        b2.clicked.connect(clear_action)

        lay1=QHBoxLayout()
        lay2=QHBoxLayout()
        lay1.addSpacing(20)
        lay1.addWidget(label1)
        lay1.addSpacing(20)
        lay2.addSpacing(20)
        lay2.addWidget(label2)
        lay2.addSpacing(20)
        lay2.addWidget(l2)
        lay2.addSpacing(20)
        
        lay3=QHBoxLayout()
        lay3.addSpacing(35)
        lay3.addWidget(b1)
        lay3.addSpacing(10)
        lay3.addWidget(b2)
        lay3.addSpacing(35)

        lay.addLayout(l1)
        lay.addSpacing(10)
        lay.addLayout(l2)
        lay.addSpacing(10)
        lay.addLayout(lay3)


        def connection_action():
            username=l1.text()
            password=l2.text()

            try:
                self.db_instance=cnt.connect(
                    host='myweb.dit.uoi.gr',
                    database='movielen',
                    user=username,
                    password=password
                )
                self.message="Host:myweb.dit.uoi.gr\n"
                self.message+="Database:movielen\n"
                self.message+='Username:{}\n'.format(username)
                self.message+='Password:{}\n'.format(password)

            except cnt.Error as e:
                self.message=str(e)
        
        def clear_action():
            l1.setText("")
            l2.setText("")




import sys
def app_exec():
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    return app.exec_()



if __name__=='__main__':
    app_exec()