from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os 


masterfile='oop-master'

class FILE:
    def __init__(self,dir,name):
        self.directory=dir
        self.name=name
    
    def __eq__(self,oth):
        return str(self.name)==str(oth.name) and str(self.directory)==str(oth.directory)



class window(QMainWindow):

    def file_founder(self,masterf):
       files=os.listdir(masterf)
       for x in files:
           if os.path.isdir(masterf+'/'+x):
              self.file_founder(masterf+'/'+x)
           else:
              self.files.append(FILE(masterf,x))
 
    def __init__(self):
        super().__init__(None)
        self.setFixedSize(800,500)
        self.setWindowTitle('OOP-CHECKER')
        self.mw=QWidget()
        self.lay=QVBoxLayout()
        self.files=[]
        self.setCentralWidget(self.mw)
        self.mw.setLayout(self.lay)
        lb=QLabel()
        lb.setFixedSize(0.96*self.width(),0.25*self.height())
        lb.setStyleSheet('background-color:black; color:white; font-size:19px;')
        lb.setAlignment(Qt.AlignCenter)
        lb.setText('ΕΛΕΓΚΤΗΣ ΟΡΘΟΤΗΤΑΣ ΑΠΟΤΕΛΕΣΜΑΤΩΝ')
        self.lay.setAlignment(Qt.AlignTop)
        self.lay.addWidget(lb)
        l1=QHBoxLayout()
        lab=QLabel()
        lab.setFixedSize(0.12*self.width(),0.1*self.height())
        lab.setPixmap(QPixmap('RESOURCES/dirs.png').scaled(lab.width(),lab.height()))
        self.file_founder(masterfile)
        self.combo=QComboBox()
        self.combo.setFixedWidth(0.25*self.width())
        self.combo.setStyleSheet('background-color:white; color:red; border:2px solid;')
        dirs=[]
        for x in self.files: 
            if x.directory not in dirs: dirs.append(x.directory)
        self.combo.addItems(dirs)
        analyze=QPushButton('ANALYZE')
        analyze.setFixedWidth(0.25*self.width())
        analyze.setStyleSheet('background-color:green; color:white;')
        analyze.clicked.connect(lambda:self.search())
        l1.setAlignment(Qt.AlignCenter)
        l1.addWidget(lab)
        l1.addWidget(self.combo)
        l1.addWidget(analyze)
        self.lay.setAlignment(Qt.AlignTop)
        self.lay.addLayout(l1)
        self.table=QTableWidget()
        self.table.setFixedSize(0.96*self.width(),0.5*self.height())
        self.table.setStyleSheet('border:null; color:blue;')
        headers=['AΡXEIO','ΦΑΚΕΛΟΣ']
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        for x in range(len(headers)):
            self.table.setColumnWidth(x,self.table.width()/len(headers))
        self.lay.addWidget(self.table)
        self.show()
    def search(self):
        searchedfiles=[x for x in self.files if x.directory==self.combo.currentText()]
        self.table.clearContents()
        self.table.setRowCount(len(searchedfiles))
        actualfiles=os.listdir(self.combo.currentText())
        for x in range(len(searchedfiles)):
            bg='green'
            it1=QTableWidgetItem()
            it1.setTextAlignment(Qt.AlignCenter)
            if searchedfiles[x].name not in actualfiles:
                bg='red'
            c1=QColor(bg)
            c1=c1.toRgb()
            it1.setBackground(c1)
            it1.setText(searchedfiles[x].name)
            it1.setFont(QFont('calibri',18))
            self.table.setItem(x,0,it1)
            it2=QTableWidgetItem()
            it2.setBackground(c1)
            it2.setTextAlignment(Qt.AlignCenter)
            it2.setFont(QFont('calibri',18))
            it2.setText(searchedfiles[x].directory)
            self.table.setItem(x,1,it2)

def main():
    a=QApplication([])
    w=window()
    return a.exec()

print('Application outcome:'+str(main()))