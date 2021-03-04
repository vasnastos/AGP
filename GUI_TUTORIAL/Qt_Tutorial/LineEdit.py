from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

#PassWord Checker By Length

passval={2:'weak',4:'good',6:'safe',7:'strong'}
passvalcolor={'weak':'red','good':'#c27689','safe':'yellow','strong':'green'}

class window(QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.setFixedSize(200,200)
        self.setWindowTitle('LineEdit Demo')
        self.mw=QWidget()
        self.lay=QVBoxLayout()
        self.lay.setAlignment(Qt.AlignCenter)
        self.mw.setLayout(self.lay)
        self.setCentralWidget(self.mw)
        self.panel1()
        self.label=QLabel()
        self.label.setFixedSize(0.8*self.width(),0.4*self.height())
        self.label.setStyleSheet('border:2px solid; font-size:19px;')
        self.lay.addWidget(self.label)

    
    def panel1(self):
        self.lay1=QHBoxLayout()
        self.ed=QLineEdit()
        self.ed.setPlaceholderText('Password Insertion')
        self.ed.setEchoMode(QLineEdit.Password)
        self.ed.textChanged.connect(lambda:self.passcode())
        self.ed.setFixedWidth(0.2*self.width())
        self.b1=QPushButton('Show')
        self.b1.setStyleSheet('background-color:lightgray; color:red; font-weight:bold; font-size:18px;')
        self.b1.clicked.connect(lambda:self.Show())
        self.b1.setFixedWidth(0.3*self.width())
        self.lay1.addWidget(self.ed)
        self.lay1.addWidget(self.b1)
        self.lay.addLayout(self.lay1)
    
    def Show(self):
        text=self.ed.text()
        QMessageBox.information(self,'Show Password','Password:'+str(text))
    
    def passcode(self):
        text=self.ed.text()
        if len(text)<=2:
            self.label.setText('Password:<b style=\"color:'+str(passvalcolor[passval[2]])+'\">'+str(passval[2])+'</b>')
        elif len(text)<=4:
            self.label.setText('Password:<b style=\"color:'+str(passvalcolor[passval[4]])+'\">'+str(passval[4])+'</b>')
        elif len(text)<=6:
            self.label.setText('Password:<b style=\"color:'+str(passvalcolor[passval[6]])+'\">'+str(passval[6])+'</b>')
        else:
            self.label.setText('Password:<b style=\"color:'+str(passvalcolor[passval[7]])+'\">'+str(passval[7])+'</b>')


def main():
    a=QApplication()
    w=window()
    w.show()
    return a.exec_()


if __name__=='__main__':
    main()