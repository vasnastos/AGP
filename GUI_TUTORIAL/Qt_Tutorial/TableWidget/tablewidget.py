from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os



class window(QMainWindow):
  def open(self):
    file=QFileDialog.getOpenFileName(self,'Open a file','.','csv files (*.csv)')
    filename=file[0]
    if len(filename)==0:
      QMessageBox.critical(self,'Error','No file selected')
      return
    self.table.clear()
    fp=QFile(filename)
    fp.open(QIODevice.ReadOnly)
    st=QTextStream(fp)
    line=st.readLine()
    data=line.split(',')
    self.table.setColumnCount(len(data))
    for x in range(len(data)-1):
      self.table.setColumnWidth(int(x),0.98*self.table.width()/len(data))
    self.table.setHorizontalHeaderLabels(data)
    size=0
    data=[]
    while not st.atEnd():
      line=st.readLine()
      size+=1
    fp.close()
    print('Size=='+str(size))
    self.table.setRowCount(size)
    fp.open(QIODevice.ReadOnly)
    st=QTextStream(fp)
    i=0
    while not st.atEnd():
      line=st.readLine()
      data=line.split(',')
      j=0
      for x in data:
        if len(x)==0:
          continue
        item=QTableWidgetItem()
        item.setText(x)
        item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(i,j,item)
        j+=1
      i+=1
    fp.close()



  def __init__(self):
    super().__init__(None)
    self.setWindowTitle('TableWidget Example')
    self.setFixedSize(600,600)
    self.mw=QWidget()
    self.lay=QVBoxLayout()
    self.setCentralWidget(self.mw)
    self.mw.setLayout(self.lay)
    self.table=QTableWidget()
    self.table.setFixedSize(0.96*self.width(),0.78*self.height())
    self.button=QPushButton('OPEN')
    self.button.setFixedWidth(0.2*self.width())
    self.button.setStyleSheet('background-color:gray; color:blue;')
    self.button.clicked.connect(lambda:self.open())
    self.lay.setAlignment(Qt.AlignCenter)
    self.lay.addWidget(self.button)
    self.lay.addWidget(self.table)


#Main Code
a=QApplication([])
w=window()
w.show()
a.exec()


