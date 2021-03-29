from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import random as r

r.seed(time.time()*1000)
countwins={'Player':0,'Computer':0}
moves={0:'R',1:'P',2:'S'}
greek_translate={'R':'ΠΕΤΡΑ','S':'ΨΑΛΙΔΙ','P':'ΧΑΡΤΙ'}
reverse_greek_translate={'ΠΕΤΡΑ':'R','ΨΑΛΙΔΙ':'S','ΧΑΡΤΙ':'P'}

computermove=''

def rps(playermove):
    global computermove
    computermove=moves[r.randint(0,2)]
    if str(playermove)==str(computermove):
        return f'ΠΑΙΚΤΗΣ:{greek_translate[playermove]}\tΥΠΟΛΟΓΙΣΤΗΣ:{greek_translate[computermove]}===ΙΣΟΠΑΛΙΑ'
    elif (str(playermove)=='R' and str(computermove)=='S') or (str(playermove)=='S' and str(computermove)=='P') or (str(playermove)=='P' and str(computermove)=='R'):
        countwins['Player']+=1
        return f'ΠΑΙΚΤΗΣ:{greek_translate[playermove]}\tΥΠΟΛΟΓΙΣΤΗΣ:{greek_translate[computermove]}===ΚΕΡΔΙΣΕ Ο ΠΑΙΚΤΗΣ'
    else:
        countwins['Computer']+=1
        return f'ΠΑΙΚΤΗΣ:{greek_translate[playermove]}\tΥΠΟΛΟΓΙΣΤΗΣ:{greek_translate[computermove]}===ΚEΡΔΙΣΕ Ο ΥΠΟΛΟΓΙΣΤΗΣ'
    

class window(QMainWindow):
    def Activate(self):
        self.opt1.setEnabled(True)
        self.opt2.setEnabled(True)
        self.opt3.setEnabled(True)
    
    def DeActivate(self):
        self.opt1.setDisabled(True)
        self.opt2.setDisabled(True)
        self.opt3.setDisabled(True)

    def __init__(self):
        super().__init__(None)
        self.setFixedSize(500,500)
        self.rcounter=0
        self.rounds=0
        self.playerchoice=''
        self.setWindowTitle('ΠΨΧ')
        self.mw=QWidget()
        self.mw.setFixedSize(self.width(),self.height())
        self.lay=QVBoxLayout()
        self.mw.setLayout(self.lay)
        self.setCentralWidget(self.mw)
        lb=QLabel()
        lb.setFixedSize(0.3*self.width(),0.1*self.height())
        lb.setStyleSheet('font-size:18px; color:blue;')
        lb.setAlignment(Qt.AlignCenter)
        lb.setText('ΑΡΙΘΜΟΣ ΓΥΡΩΝ')
        self.combo=QComboBox()
        self.combo.setFixedWidth(0.5*self.width())
        self.combo.setStyleSheet('color:blue; font-size:17px; border:2px solid;')
        self.combo.activated.connect(lambda:self.SetRounds())
        rounds=[str(x) for x in range(1,11)]
        self.combo.addItems(rounds)
        sublay=QHBoxLayout()
        sublay.addWidget(lb)
        sublay.addWidget(self.combo)
        self.lay.setAlignment(Qt.AlignTop)
        self.lay.addLayout(sublay)
        self.score=QLabel()
        self.score.setStyleSheet('font-weight:bold; font-size:16px; color:black;')
        self.score.setFixedSize(0.6*self.width(),0.2*self.height())
        self.score.setAlignment(Qt.AlignCenter)
        self.score.setText('Σκορ:0-0')
        anotherWidget=QWidget()
        anotherWidget.setFixedSize(0.26*self.width(),0.2*self.height())
        anotherwidgetlayout=QVBoxLayout()
        anotherWidget.setLayout(anotherwidgetlayout)
        self.opt1=QRadioButton('ΠΕΤΡΑ',self)
        self.opt1.setFixedWidth(0.7*anotherWidget.width())
        self.opt2=QRadioButton('ΨΑΛΙΔΙ',self)
        self.opt1.setFixedWidth(0.7*anotherWidget.width())
        self.opt3=QRadioButton('ΧΑΡΤΙ',self)
        self.opt3.setFixedWidth(0.7*anotherWidget.width())
        self.opt1.setStyleSheet('text-align:center; font-weight:bold;')
        self.opt2.setStyleSheet('text-align:center; font-weight:bold;')
        self.opt3.setStyleSheet('text-align:center; font-weight:bold;')
        self.opt1.clicked.connect(lambda:self.Option())
        self.opt2.clicked.connect(lambda:self.Option())
        self.opt3.clicked.connect(lambda:self.Option())
        self.DeActivate()
        anotherwidgetlayout.setAlignment(Qt.AlignTop)
        anotherwidgetlayout.addWidget(self.opt1)
        anotherwidgetlayout.addWidget(self.opt2)
        anotherwidgetlayout.addWidget(self.opt3)
        l2=QHBoxLayout()
        l2.addWidget(self.score)
        l2.addSpacing(10)
        l2.setAlignment(Qt.AlignCenter)
        l2.addWidget(anotherWidget)
        self.lay.setAlignment(Qt.AlignTop)
        self.lay.addLayout(l2)
        l3=QHBoxLayout()
        self.computer=QLabel()
        self.computer.setFixedSize(0.6*self.width(),0.05*self.height())
        self.computer.setAlignment(Qt.AlignCenter)
        self.computer.setStyleSheet('font-weight:bold; font-size:18px;')
        self.computer.setText('Ο Αντίπαλος έπαιξε:')
        self.stack=QStackedWidget()
        self.stack.setFixedSize(0.26*self.width(),0.07*self.height())
        gamebutton=QPushButton('ΠΑΙΞΕ')
        resetButton=QPushButton('ΕΠΑΝΑΦΟΡΑ')
        resetButton.setFixedWidth(0.8*self.stack.width())
        gamebutton.setFixedWidth(0.8*self.stack.width())
        gamebutton.setStyleSheet('background-color:gray; color:blue; font-size:15px; font-weight:bold;')
        resetButton.setStyleSheet('background-color:black; color:red; font-size:15px; font-weight:bold;')
        gamebutton.clicked.connect(lambda:self.round())
        resetButton.clicked.connect(lambda:self.reset())
        self.stack.addWidget(gamebutton)
        self.stack.addWidget(resetButton)
        l3.setAlignment(Qt.AlignTop)
        l3.addWidget(self.computer)
        l3.addSpacing(20)
        l3.addWidget(self.stack)
        self.lay.setAlignment(Qt.AlignTop)
        self.lay.addLayout(l3)
        self.result=QTextEdit()
        self.result.setFixedSize(0.96*self.width(),0.45*self.height())
        self.result.setStyleSheet('border:2px solid blue; color:black; font-size:17px; font-weight:bold;')
        self.result.setAlignment(Qt.AlignLeft)
        self.result.setText('<center>ΑΠΟΤΕΛΕΣΜΑΤΑ</center><hr><ul>')
        self.lay.setAlignment(Qt.AlignTop)
        self.lay.addWidget(self.result)
    
    def round(self):
        if self.rounds==0:
            QMessageBox.critical(self,'Round 0','Please select number of rounds')
            return
        text=self.result.toHtml()
        text+='<li>'+str(rps(reverse_greek_translate[self.playerchoice]))+'</li>'
        self.score.setText(f'ΣΚΟΡ:{countwins["Player"]}-{countwins["Computer"]}')
        self.computer.setText(f'Ο Αντίπαλος έπαιξε:{greek_translate[computermove]}')
        self.rcounter+=1
        if self.rcounter>self.rounds:
          text+='</ul>'
          self.stack.setCurrentIndex(1)
          self.DeActivate()
          message=f'<html><body><h2>Results</h2><hr><b style="color:black; font-size:16px;">Player Wins:{countwins["Player"]}\tComputer Wins:{countwins["Computer"]}<br>\t<b style="color:red;">Winner:{"Player" if countwins["Player"]>countwins["Computer"] else "Computer" if countwins["Player"]<countwins["Computer"] else "Tie Game"}'
          QMessageBox.information(self,'Outcome',message)
        self.result.setText(text)
    
    def SetRounds(self):
       self.Activate()
       self.rounds=int(self.combo.currentText()) 
       self.combo.setDisabled(True)
       print('Rounds:'+str(self.rounds))

    def Option(self):
        selected=QObject.sender(self)
        print(selected.text())
        self.playerchoice=selected.text()
    
    def reset(self):
        self.DeActivate()
        self.rounds=0
        self.rcounter=1
        countwins['Player']=0
        countwins['Computer']=0
        self.score.setText('ΣΚΟΡ:0-0')
        self.computer.setText('Ο Αντίπαλος έπαιξε')
        self.combo.setEnabled(True)
        self.stack.setCurrentIndex(0)
        self.result.setText('<h2>ΑΠΟΤΕΛΕΣΜΑ</h2><hr>')


a=QApplication([''])
w=window()
w.show()
a.exec()



