from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Pyqt5.QtCore import *
import sys

class window(QMainWindow):
    def make_menu(self):
        self.menu=QMenu()
        self.menu.setIcon(QIcon('./Menu_project/menu.png'))
        self.menuBar().addMenu(self.menu)
        a1=QAction('OPEN',self)
        a1.triggered.connect(lambda:self.menuslot('OPEN'))
        self.menu.addAction(a1)
        a2=QAction('SAVE',self)
        a2.triggered.connect(lambda:self.menuslot('SAVE'))
        self.menu.addAction(a2)
        a3=QAction('QUIT',self)
        a3.triggered.connect(lambda:self.menuslot('QUIT'))
        self.menu.addAction(a3)
        
    def __init__(self):
        super().__init__(None)
        self.setFixedSize(250,100)
        self.setWindowTitle('Menu Demo')
        self.mw=QWidget()
        self.lay=QVBoxLayout()
        self.mw.setLayout(self.lay)
        self.setCentralWidget(self.mw)
        self.make_menu()
        self.label=QLabel()
        self.label.setFixedSize(0.96*self.width(),0.6*self.height())
        self.label.setPixmap(QPixmap('./Menu_project/men.png').scaled(self.label.width(),self.label.height()))
        self.label.setStyleSheet('border:2px solid;')
        self.lay.addWidget(self.label)

    def menuslot(self,a):
        if str(a)=='OPEN':
            QMessageBox.information(self,'Open Triggerd','<b style=\"color:red; font-size:21px;\">Open Value Triggered</b>')
        elif str(a)=='SAVE':
            QMessageBox.information(self,'Open Triggerd','<b style=\"color:blue; font-size:21px;\">Save Value Triggered</b>')
        else:
            i=QMessageBox.information(self,'Open Triggerd','<b style=\"color:green; font-size:21px;\">Open Value Triggered<br>Do you want to Exit App</b>',QMessageBox.Yes,QMessageBox.No)
            if int(i)==QMessageBox.Yes:
                sys.exit(0)               


a=QApplication([])
w=window()
w.show()
a.exec()