from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random as r
import PyQt5.QtCore as qgt

#Genarate a random number from zero to thousand

class window(QMainWindow):
   def __init__(self):
        QMainWindow.__init__(self,None)
        self.setFixedSize(200,200)
        self.setWindowTitle('Button Tutorial')
        self.mainwidget=QWidget()
        self.setCentralWidget(self.mainwidget)
        self.lay=QVBoxLayout()
        self.lay.setAlignment(qgt.Qt.AlignCenter)
        self.mainwidget.setLayout(self.lay)
        self.buttonpanel()
   
   def buttonpanel(self):
        self.button=QPushButton('PRESS')
        self.button.clicked.connect(lambda:self.press())
        self.lay.addWidget(self.button)
   def  press(self):
       QMessageBox.information(self,'Button Event','<b style=\"font-size:20px; color:blur;\">Random Number Genarated:'+str(r.randint(0,1000))+'</b>') 


def main():
    a=QApplication([])
    w=window()
    w.show()
    return a.exec()

if __name__=='__main__':
    main()
