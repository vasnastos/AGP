from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Todo List")
        self.setFixedSize(600,600)
        w=QWidget()
        self.layout_manager=QVBoxLayout()
        self.setCentralWidget(w)
        w.setFixedSize(self.width(),self.height())
        w.setLayout(self.layout_manager)
        self.panel1()
        self.panel2()
        self.panel3()
    
    def panel1(self):
        self.tlist=QListWidget(self)
        self.tlist.setFixedSize(int(0.97*self.width()),int(0.46*self.height()))
        self.tlist.setStyleSheet("border:2px solid black;")
        self.layout_manager.addWidget(self.tlist)

    def panel2(self):
        self.layout_manager.addSpacing(40)
        self.l1=QHBoxLayout()
        self.task=QLineEdit(self)
        self.task.setFixedWidth(int(0.97*self.width()))
        self.task.setStyleSheet("""
                                QLineEdit{ 
                                        background-color:rgb(202, 255, 227);
                                        border: 2px solid gray;
                                        border-radius: 10px;
                                        padding: 0 8px;
                                        selection-background-color: darkgray;
                                        font-size: 16px;}
                                        QLineEdit:focus { 
                                        background-color:rgb(192, 192, 255);}
                                """)
        self.layout_manager.addWidget(self.task)
    
    def panel3(self):
        self.layout_manager.setSpacing(40)
        b1=QPushButton("ADD",self)
        b2=QPushButton("DELETE",self)
        b3=QPushButton("IMPORT TASK",self)
        b4=QPushButton("EXPORT TASK",self)


        b1.setFixedWidth(int(0.2*self.width()))
        b1.setFixedHeight(int(0.05*self.height()))
        b2.setFixedWidth(int(0.2*self.width()))
        b2.setFixedHeight(int(0.05*self.height()))
        b3.setFixedWidth(int(0.2*self.width()))
        b3.setFixedHeight(int(0.05*self.height()))
        b4.setFixedWidth(int(0.2*self.width()))
        b4.setFixedHeight(int(0.05*self.height()))


        b1.setStyleSheet(
            """
            QPushButton
            {
                color:white;
                font-weight:bold;
                font-size:14px;
                border-radius:50%;
                background-color:#32357a;
            }

            QPushButton:hover
            {
                color:#32357a;
                font-size:16px;
                text-decoration:underline;
                background-color:white;
                border:2px solid red;
            }
            """
        )

        b2.setStyleSheet(
            """
             QPushButton
            {
                color:white;
                font-weight:bold;
                font-size:14px;
                border-radius:50%;
                background-color:#32357a;
            }

            QPushButton:hover
            {
                color:#32357a;
                font-size:16px;
                text-decoration:underline;
                background-color:white;
                border:2px solid red;
            }
            """
        )

        b3.setStyleSheet(
            """
            QPushButton
            {
                color:white;
                font-weight:bold;
                font-size:14px;
                border-radius:50%;
                background-color:#32357a;
            }

            QPushButton:hover
            {
                color:#32357a;
                font-size:16px;
                text-decoration:underline;
                background-color:white;
                border:2px solid red;
            }
            """
        )

        b4.setStyleSheet(
            """
             QPushButton
            {
                color:white;
                font-weight:bold;
                font-size:14px;
                border-radius:50%;
                background-color:#32357a;
            }

            QPushButton:hover
            {
                color:#32357a;
                font-size:16px;
                text-decoration:underline;
                background-color:white;
                border:2px solid red;
            }
            """
        )

        b1.clicked.connect(lambda:self.add_task())
        b2.clicked.connect(lambda:self.delete_item())
        b3.clicked.connect(lambda:self.load_item())
        b4.clicked.connect(lambda:self.save_items())

        l1=QHBoxLayout()
        l1.addWidget(b1)
        l1.setSpacing(30)
        l1.addWidget(b2)
        l1.setSpacing(30)
        l1.addWidget(b3)
        l1.setSpacing(30)
        l1.addWidget(b4)
        l1.setSpacing(30)

        self.layout_manager.addLayout(l1)

        

    def add_task(self):
        if len(self.task.text())==0: 
            QMessageBox.critical(self,"Error On number insertion","Please Insert a non blank field")
            return
        self.tlist.addItem(self.task.text())
    
    def delete_item(self):
        items_selected=self.tlist.selectedItems()
        if len(items_selected)==0: return
        _=[self.tlist.takeItem(self.tlist.row(it)) for it in items_selected]

    def load_item(self):
        fn=QFileDialog.getOpenFileName(self,'Select Tasks','.','*.txt')
        if len(fn[0])!=0:
           fp=QFile(fn[0])
           fp.open(QIODevice.ReadOnly)
           stream=QTextStream(fp)
           while not stream.atEnd():
               data=stream.readLine().strip()
               self.tlist.addItem(data)
           fp.close() 

    def save_items(self):
        fn=QFileDialog.getSaveFileName(self,'Save Tasks','.','*.txt')
        if len(fn[0])!=0:
            fp=QFile(fn[0])
            fp.open(QIODevice.WriteOnly)
            stream=QTextStream(fp)
            for i in range(self.tlist.count()):
                stream<<str(self.tlist.item(i).text())<<"\n"
            fp.close()

import sys
if __name__=='__main__':
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    sys.exit(app.exec_())