# pip install pyside6-->Qt Widgets
import random
import sys
# pip install pyside6
from PySide6.QtCore import Qt, Slot, SIGNAL, QObject, QFile, QTextStream, QIODevice
import PySide6.QtGui as qgt
import PySide6.QtWidgets as qt
import os

class Text:
        start = '<html><head><style>body{background-color:white; color:blue; font-weight:bold; text-align:center; font-size:18px;}</style></head><body><h1>Inserted values</h1><hr style=\"border-top:2px solid green;\"><ul>'
        listcontainers = ""
        end = '</ul></body></html>'
        shown = start+listcontainers+end

def renew(stream):
        Text.listcontainers = stream
        Text.shown = Text.start+Text.listcontainers+Text.end

class App(qt.QMainWindow):
        def open_File(self):
            listcont = ''
            filename = os.getcwd()+'\\values.txt'
            fp = QFile(filename)
            fp.open(QIODevice.ReadOnly)
            stream = QTextStream(fp)
            while not stream.atEnd():
                line = stream.readLine()
                data = line.split(',')
                listcont += '<li>'+str(data[0])+'---'+str(data[1])+'</li>'
            fp.close()
            """ 
                Εναλλακτικός Τρόπος 
                ::y=open(filename,'r') 
                for k in y: 
                    data=k.split(',') 
                    listcont+='<li>'+str(data[0])+'---'+str(data[1])+'</li>' 
                y.close() 
                """
            renew(listcont)

        def __init__(self):
            self.text = 'Hello world from command line'
            qt.QMainWindow.__init__(self, None)
            self.mainwidget = qt.QWidget()
            self.setFixedSize(400, 600)
            self.setWindowTitle('Tutorial App')
            self.setWindowIcon(qgt.QIcon('RESOURCES/tutorial.png'))
            self.setCentralWidget(self.mainwidget)
            self.l = qt.QVBoxLayout()
            self.textarea = qt.QTextEdit()
            self.mainwidget.setLayout(self.l)
            self.label = qt.QLabel()
            # self.bar=qt.QScrollBar(self.label)
            self.l.setSpacing(10)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setFixedSize(0.96*self.width(), 0.45*self.height())
            self.label.setStyleSheet(
                'float:left; border:2px solid red; color:white; background-color:black; font-size:18px;')
            self.label.setText('<html>Hello World from Qt Creator <br>Using Python<br>>Here we got some useful widgets:<ul><li>QSlider</li><li>QPushButton</li><li>QLineEdit</li><li>QSpinBox</li><li>QComboBox</li><li>QFile-QTextStream</li></ul></html>')
            self.l.addWidget(self.label)
            self.button = qt.QPushButton('Connect')
            self.button.setFixedWidth(0.2*self.width())
            self.button.setStyleSheet(
                'color:red; text-align:center; border-radious:16px; background-color:gray;')
            self.button.clicked.connect(lambda: self.act())
            self.combo = qt.QComboBox()
            list = ['Samsung', 'Apple', 'Microsoft', 'Nokia']
            self.combo.addItems(list)
            self.combo.activated.connect(lambda: self.comboAction())
            self.combo.setFixedWidth(0.2*self.width())
            self.l1 = qt.QHBoxLayout()
            self.slider = qt.QSlider()
            self.box = qt.QDoubleSpinBox()
            self.box.setRange(0, 100)
            self.box.setToolTip('DoubleSpinBox')
            self.box.setSingleStep(0.24)
            self.box.setFixedWidth(0.2*self.width())
            self.slider.setOrientation(Qt.Horizontal)
            self.slider.setFixedWidth(0.3*self.width())
            self.slider.sliderReleased.connect(lambda: self.slideEvent())
            # signals-->valueChanged,sliderMoved
            self.slider.setRange(0, 100)
            self.slider.setTickInterval(1)
            self.l.addLayout(self.l1)
            self.l1.addWidget(self.button)
            self.l1.addWidget(self.combo)
            self.l1.addWidget(self.slider)
            self.lineedit = qt.QLineEdit()
            self.lineedit.setFixedWidth(0.2*self.width())
            self.button2 = qt.QPushButton()
            self.button2.setText("Add")
            self.button2.setFixedWidth(0.2*self.width())
            self.button2.clicked.connect(lambda: self.values())
            self.l2 = qt.QHBoxLayout()
            self.l2.addWidget(self.box)
            self.l2.addWidget(self.lineedit)
            self.l2.addWidget(self.button2)
            self.l.addLayout(self.l2)
            self.l3 = qt.QHBoxLayout()
            self.textarea.setFixedWidth(0.96*self.width())
            self.textarea.setFixedHeight(0.35*self.height())
            self.textarea.setStyleSheet('border:2px solid yellow;')
            self.open_File()
            self.textarea.setText(Text.shown)
            self.l3.addWidget(self.textarea)
            self.l.addLayout(self.l3)

            # Other Layout forms
            # QStackedLayout,QGridLayout
        # Slots For Actions
        def act(self):
            qt.QMessageBox.information(
                self, 'clicked Button', 'Button Selected')

        def comboAction(self):
            selectedtext = self.combo.currentText()
            selectedposition = self.combo.currentIndex()
            qt.QMessageBox.information(self, 'ComboBox Activated', '<html><hr style=\"border-top:2px solid red;\"><table border=\"3\"><tr><th>Action</th><th>Value</th></tr><tr><td>Text</td><td>'+str(
                selectedtext)+'</td></tr><tr><td>Index</td><td>'+str(selectedposition)+'</td></tr></table></html>')

        def slideEvent(self):
            qt.QMessageBox.information(
                self, 'Slider Moved', 'Slider Value:'+str(self.slider.value()))

        def values(self):
            Text.listcontainers += '<li>' + \
                str(self.lineedit.text())+'---'+str(self.box.text())+'</li>'
            renew(Text.listcontainers)
            self.textarea.setText(Text.shown)
            print('Value Added')
