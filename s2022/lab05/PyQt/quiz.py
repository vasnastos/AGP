from re import S
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
import os,sys
import mysql.connector as cnt


class Question:
    def __init__(self,inp,ansrs=None):
        self.question=inp
        self.answers={} if ansrs==None else ansrs
    
    def answer(self,ans_name,is_correct=False):
        self.answers[ans_name]=is_correct
    
    def get_correct_answer(self):
        return [ans_name for ans_name,accuracy in self.answers.items() if accuracy][0]


class Question_Pool:
    def __init__(self):
        self.questions=[]
    
    def load(self):
        connector=cnt.connect(
            host='myweb.dit.uoi.gr',
            database='AGP',
            user='agproot',
            password='!Ditagp2022'
        )
        cursor=connector.cursor()
        query='SELECT * FROM quiz'
        cursor.execute(query)
        records=cursor.fetchall()
        connector.close()

        return [Question(record[0],{record[0]:record[i]==record[len(record)] for i in range(1,len(record)-1)}) for record in records]

class Frame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        w=QWidget()
        w.setFixedSize(w.width(),w.height())
        w.setFixedSize(self.width(),self.height())
        self.layout_manager=QVBoxLayout()
        self.setCentralWidget(w)
        self.setWindowIcon(QIcon(os.path.join('','img','quiz_central.png')))
        self.setWindowTitle("Quiz Game")
        w.setFixedSize(self.width(),self.height())
        w.setLayout(self.layout_manager)
        self.panel1()
        self.panel2()
        self.panel3()

    def showtime(self):
        self.count-=1
        if self.count==0:
            self.count=20
            self.timer.stop()
        self.countdown.setText(str(self.count)+'`s')
        

    def panel1(self):
        # self.timer=QTimer(self.panel1())
        self.count=20
        # self.timer.timeout.connect(self.showtime)
        self.countdown=QLabel()
        self.countdown.setStyleSheet(
            """
            QLabel{
                border:2px solid red;
                font-size:15px;
                font-weight:bold;
            }
            """
        )
        self.countdown.setFixedWidth(int(0.16*self.width()))
        self.countdown.setAlignment(Qt.AlignCenter)
        self.countdown.setText(str(self.count)+'`s')

        question_label=QLabel()
        question_label.setFixedSize(int(0.75*self.width()),int(0.25*self.height()))
        question_label.setStyleSheet("""
                                        QLabel{
                                            border:3px solid;
                                            font-family:swiss;
                                            font-weight:bold;
                                            font-size:16px;
                                        }
                                     """)
        question_label.setAlignment(Qt.AlignCenter)
        panel_layout=QHBoxLayout()
        panel_layout.addSpacing(5)
        panel_layout.addWidget(question_label,0,Qt.AlignTop)
        panel_layout.addSpacing(5)
        panel_layout.addWidget(self.countdown,0,Qt.AlignTop)
        self.layout_manager.addLayout(panel_layout,)

    
    def panel2(self):
        panel_layout=QHBoxLayout()
        panel_layout.addSpacing(100)
        self.buttons=[]
        for _ in range(4):
            self.buttons.append(QRadioButton())
        
        for b in self.buttons:
            panel_layout.addWidget(b,0,Qt.AlignTop)
            panel_layout.addSpacing(10)
        
        panel_layout.addSpacing(20)
        self.layout_manager.addLayout(panel_layout)

    def panel3(self):
        panel_layout=QHBoxLayout()
        b1=QPushButton("SUBMIT")
        b1.setFixedWidth(int(0.2*self.width()))
        b1.setStyleSheet(
            """
            QPushButton{
                background-color:#4150c4;
                color:#cbd4cc;
                font-size:15px;
                font-weight:bold;
            }
            """
        )
        b2=QPushButton("NEXT")
        b2.setFixedWidth(int(0.2*self.width()))
        b2.setStyleSheet(
            """
            QPushButton{
                background-color:#4150c4;
                color:#cbd4cc;
                font-size:15px;
                font-weight:bold;
            }
            """
        )

        panel_layout.addSpacing(40)
        panel_layout.addWidget(b1,0,Qt.AlignTop)
        panel_layout.addSpacing(10)
        panel_layout.addWidget(b2,0,Qt.AlignTop)
        panel_layout.addSpacing(40)
        self.layout_manager.addLayout(panel_layout)


def application():
    app=QApplication(sys.argv)
    f=Frame()
    f.show()
    return app.exec_()

if __name__=='__main__':
    application()