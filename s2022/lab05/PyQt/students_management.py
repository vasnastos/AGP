from re import S
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3 as sql
import sys


class Database:
    def __init__(self):
        self.connector=sql.connect("students.db")
        cursor=self.connector.cursor()
        query="CREATE TABLE IF NOT EXISTS STUDENT(name VARCHAR(80),lastname VARCHAR(80),am VARCHAR(10),semester INTEGER,email TEXT,PRIMARY KEY(am))"
        cursor.execute(query)
        self.connector.commit() 
        
    def insert_student(self,student_name,student_lastname,student_am,student_semester,student_email):
        query="INSERT INTO STUDENT(name,lastname,am,semester,email) VALUES(?,?,?,?,?)"
        cursor=self.connector.cursor()
        try:
            cursor.execute(query,(student_name,student_lastname,student_am,int(student_semester),student_email))
        except sql.Error as e:
            print(e)
        self.connector.commit()
    
    def get_students(self):
        query="SELECT * FROM STUDENT"
        cursor=self.connector.cursor()
        cursor.execute(query)
        rec=list(cursor.fetchall())
        return rec

    def get_description(self):
        query="SELECT * FROM STUDENT"
        cursor=self.connector.cursor()
        cursor.execute(query)
        description=cursor.description
        return description
    
    def record_exist(self,am_val:str):
        query="SELECT * FROM STUDENT WHERE am=?"
        cursor=self.connector.cursor()
        cursor.execute(query,(am_val,))
        val_record=cursor.fetchall()
        return val_record!=None
    
    def close(self):
        self.connector.close()

class HPushButton(QPushButton):

    mouseHover=pyqtSignal(bool)

    def __init__(self,title=""):
        QPushButton.__init__(self)
        self.setMouseTracking(True)
        self.setText(title)
    
    def enterEvent(self, event):
        self.mouseHover.emit(True)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def leaveEvent(self, event):
        self.mouseHover.emit(False)
        self.setCursor(QCursor(Qt.ArrowCursor))


class Frame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(700,700)
        self.setWindowTitle("Students Management System")
        w=QWidget()
        w.setFixedSize(self.width(),self.height())
        self.layout_manager=QVBoxLayout()
        w.setLayout(self.layout_manager)
        self.setCentralWidget(w)
        self.db_obj=Database()
        self.panel1()
        self.panel2()
        self.table_renew()

    def __del__(self):
        self.db_obj.close()
        

    def panel1(self):
        self.edit_name=QLineEdit()
        self.edit_lastname=QLineEdit()
        self.edit_semester=QLineEdit()
        self.edit_am=QLineEdit()
        self.edit_mail=QLineEdit()

        name_label=QLabel("STUDENT`S NAME")
        lastname_label=QLabel("STUDENT`S LASTNAME")
        semester_label=QLabel("STUDENT`S SEMESTER")
        am_label=QLabel("STUDENT`S AM")
        mail_label=QLabel("MAIL LABEL")


        name_label.setFixedWidth(int(0.34*self.width()))
        lastname_label.setFixedWidth(int(0.34*self.width()))
        am_label.setFixedWidth(int(0.34*self.width()))
        semester_label.setFixedWidth(int(0.34*self.width()))
        mail_label.setFixedWidth(int(0.34*self.width()))


        self.edit_name.setFixedWidth(int(0.34*self.width()))
        self.edit_lastname.setFixedWidth(int(0.34*self.width()))
        self.edit_semester.setFixedWidth(int(0.34*self.width()))
        self.edit_am.setFixedWidth(int(0.34*self.width()))
        self.edit_mail.setFixedWidth(int(0.34*self.width()))


        name_label.setStyleSheet(
            """
            QLabel
            {
                font-size:14px;
                color:blue;
                font-weight:bold;
            }
            """
        )

        lastname_label.setStyleSheet(
            """
            QLabel{
                font-size:14px solid;
                color:blue;
                font-weight:bold;
            }
            """
        )

        semester_label.setStyleSheet("""
            QLabel{
                font-size:14px;
                color:blue;
                font-weight:bold;
            }
        """)
        am_label.setStyleSheet("""
            QLabel{
                font-size:14px;
                color:blue;
                font-weight:bold;
            }
        """)

        mail_label.setStyleSheet("""
            QLabel{
                font-size:14px;
                color:blue;
                font-weight:bold;
            }
        """)

        self.edit_name.setStyleSheet(
            """
            QLineEdit{
                color:black;
                border:2px solid;
                font-size:16px;
                font-weight:bold;
            }
            """
        )
        self.edit_lastname.setStyleSheet("""
            QLineEdit{
                color:black;
                border:2px solid;
                font-size:16px;
                font-weight:bold;
            }
            """)
        self.edit_semester.setStyleSheet(
            """
            QLineEdit{
                color:black;
                border:2px solid;
                font-size:16px;
                font-weight:bold;
            }
            """
        )
        self.edit_am.setStyleSheet(
            """
            QLineEdit{
                color:black;
                border:2px solid;
                font-size:16px;
                font-weight:bold;
            }
            """
        )
        self.edit_mail.setStyleSheet(
            """
            QLineEdit{
                color:black;
                border:2px solid;
                font-size:16px;
                font-weight:bold;
            }
            """
        )    
        b1=HPushButton("INSERT")
        b2=HPushButton("CLEAR")
        b1.setFixedSize(int(0.24*self.width()),int(0.05*self.height()))
        b2.setFixedSize(int(0.24*self.width()),int(0.05*self.height()))
        b1.setStyleSheet(
            """
            QPushButton{
                color:white;
                background-color:#2b3a8f;
                font-size:12px;
                font-weight:bold;
                border:2px solid;
            }

            QPushButton:hover
            {
                color:#2b3a8f;
                background-color:white;
                font-size:12px;
                font-weight:bold;
            }
            """
        )
        b2.setStyleSheet(
            """
            QPushButton{
                color:white;
                background-color:#2b3a8f;
                font-size:12px;
                font-weight:bold;
                border:2px solid;
            }

            QPushButton:hover
            {
                color:#2b3a8f;
                background-color:white;
                font-size:12px;
                font-weight:bold;
            }
            """
        )

        b1.clicked.connect(self.insert_action)
        b2.clicked.connect(self.clear_action)

        l1=QHBoxLayout()
        l2=QHBoxLayout()
        l3=QHBoxLayout()
        l4=QHBoxLayout()
        l5=QHBoxLayout()
        l6=QHBoxLayout()

        l1.addSpacing(10)
        l1.addWidget(name_label)
        l1.addSpacing(10)
        l1.addWidget(self.edit_name)
        l1.addSpacing(10)

        l2.addSpacing(10)
        l2.addWidget(lastname_label)
        l2.addSpacing(10)
        l2.addWidget(self.edit_lastname)
        l2.addSpacing(10)

        l3.addSpacing(10)
        l3.addWidget(am_label)
        l3.addSpacing(10)
        l3.addWidget(self.edit_am)
        l3.addSpacing(10)

        l4.addSpacing(10)
        l4.addWidget(semester_label)
        l4.addSpacing(10)
        l4.addWidget(self.edit_semester)
        l4.addSpacing(10)

        l5.addSpacing(10)
        l5.addWidget(mail_label)
        l5.addSpacing(10)
        l5.addWidget(self.edit_mail)
        l5.addSpacing(10)

        l6.addSpacing(30)
        l6.addWidget(b1)
        l6.addSpacing(15)
        l6.addWidget(b2)
        l6.addSpacing(30)

        self.layout_manager.addLayout(l1)
        self.layout_manager.addSpacing(10)
        self.layout_manager.addLayout(l2)
        self.layout_manager.addSpacing(10)
        self.layout_manager.addLayout(l3)
        self.layout_manager.addSpacing(10)
        self.layout_manager.addLayout(l4)
        self.layout_manager.addSpacing(10)
        self.layout_manager.addLayout(l5)
        self.layout_manager.addSpacing(10)
        self.layout_manager.addLayout(l6)
        self.layout_manager.addSpacing(10)
    
    def panel2(self):
        self.table_view=QTableWidget()
        self.table_view.setFixedSize(int(0.97*self.width()),int(0.45*self.height()))
        self.table_view.setAutoFillBackground(True)
        self.table_view.setStyleSheet(
            """
            QTableWidget{
                font-weight:bold;
                background-color:#acb3b5;
            }
            """
        )
        self.layout_manager.addWidget(self.table_view)
    
    def insert_action(self):
        if len(self.edit_name.text())==0 or len(self.edit_lastname.text())==0 or len(self.edit_am.text())==0 or len(self.edit_semester.text())==0 or len(self.edit_mail.text())==0:
            QMessageBox.critical(self,"Empty Field","Please fill all the insertion fields")
            return
        print('is here')
        try:
            self.db_obj.insert_student(self.edit_name.text(),self.edit_lastname.text(),self.edit_am.text(),self.edit_semester.text(),self.edit_mail.text())
        except sql.Error as e:
            print(e)
        self.table_renew()

    def clear_action(self):
        self.edit_name.clear()
        self.edit_lastname.clear()
        self.edit_am.clear()
        self.edit_semester.clear()
        self.edit_mail.clear()

    def table_renew(self):
        records=self.db_obj.get_students()
        columns=[c[0] for c in self.db_obj.get_description()]
        self.table_view.clear()
        self.table_view.setRowCount(len(records))
        self.table_view.setColumnCount(len(columns))
        self.table_view.setHorizontalHeaderLabels([c.upper() for c in columns])
        for i in range(len(columns)):
            self.table_view.setColumnWidth(i,self.table_view.width()//len(columns))
        for index,row in enumerate(records):
            for i in range(len(columns)):
                item=QTableWidgetItem(str(row[i]))
                item.setForeground(QColor("#194023"))
                f=QFont()
                f.setBold(True)
                f.setPointSize(14)
                item.setFont(f)
                self.table_view.setItem(index,i,item)
        
    def hover_button(self):
        self.setCursor(QCursor(Qt.PointingHandCursor))


if __name__ == "__main__":
    app=QApplication(sys.argv)
    f=Frame()
    f.show()
    app.exec_()