import requests,re,sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Lexicon:
    def __init__(self):
        words_text=requests.get("https://www.mit.edu/~ecprice/wordlist.10000").text.strip()
        self.words=[w.strip() for w in words_text.split("\n")]

    def __len__(self):
        return len(self.words)

    def word_length(self,potential_l):
        return [word for word in self.words if len(word)==potential_l]
    
    def starts_with(self,startw:str):
        return [word for word in self.words if word.startswith(startw)]
    
    def ends_with(self,endw):
        return [word for word in self.words if word.endswith(endw)]
    
    def contains(self,seq,times):
        return [word for word in self.words if re.search('.*('+seq+'){'+str(times)+'}.*',word)]
    
    def find(self,seq):
        return [word for word in self.words if re.search('.*'+seq.replace('-','.')+'.*',word)]

class Frame(QMainWindow):
    def __init__(self):
      QMainWindow.__init__(self)
      self.lexicon=Lexicon()
      self.setWindowTitle("Lexicon")
      self.setFixedSize(690,600)
      w=QWidget()
      w.setFixedSize(self.width(),self.height())
      self.layout_manager=QVBoxLayout()
      w.setLayout(self.layout_manager)
      self.setCentralWidget(w)
      lb=QLabel()
      lb.setText("LEXICON APPLICATION")
      lb.setFixedSize(int(0.97*self.width()),int(0.13*self.height()))
      lb.setAlignment(Qt.AlignCenter)
      lb.setStyleSheet(
          """
          QLabel{
              color:black;
              font-weight:bold;
              font-size:15px;
              border:2px solid black;
          }
          """
      )
      self.layout_manager.addWidget(lb)
      self.panel1()

    
    def panel1(self):
        lay=QHBoxLayout()
        b1=QRadioButton()
        b1.setProperty("id",1)
        b1.setStyleSheet(
            """
            QRadioButton{
                color:black;
                font-weight:bold;
                font-size:14px;
            }
            """
        )
        b1.setText("SEARCH BY LENGTH")
        b2=QRadioButton("SEARCH BY START SEQUENCE")
        b2.setProperty("id",2)
        b2.setStyleSheet("""
            QRadioButton{
                color:black;
                font-weight:bold;
                font-size:14px;
            }
        """)
        b3=QRadioButton("SEARCH BY END SEQUENCE")
        b3.setProperty("id",3)
        b3.setStyleSheet("""
            QRadioButton{
                color:black;
                font-weight:bold;
                font-size:14px;
            }
        """)
        b4=QRadioButton("SEARCH BY REPITITIONS OF SEQUENCE")
        b4.setProperty("id",4)
        b4.setStyleSheet("""
            QRadioButton{
                color:black;
                font-weight:bold;
                font-size:14px;
            }
        """)
        b5=QRadioButton("SEARCH BY SEQUENCE")
        b5.setProperty("id",5)
        b5.setStyleSheet("""
            QRadioButton{
                color:black;
                font-weight:bold;
                font-size:14px;
            }
        """)

        for b in [b1,b2,b3,b4,b5]:
            b.clicked.connect(self.checkbutton)

        lay.addSpacing(10)
        lay.addWidget(b1)
        lay.addSpacing(10)
        lay.addWidget(b2)
        lay.addSpacing(10)
        lay.addWidget(b3)
        lay1=QHBoxLayout()
        lay1.addSpacing(10)
        lay1.addWidget(b4)
        lay1.addSpacing(10)
        lay1.addWidget(b5)
        self.layout_manager.addLayout(lay)
        self.layout_manager.addLayout(lay1)

        self.textEdit=QTextEdit()
        self.textEdit.setFixedSize(int(0.97*self.width()),int(0.45*self.height()))
        self.textEdit.setStyleSheet("""
         QTextEdit{
             color:black;
             font-weight:bold;
             font-size:15px;
         }
        """)
        self.layout_manager.addWidget(self.textEdit)


    def checkbutton(self):
        b=int(self.sender().property("id"))
        words=[]
        search_sequence=''
        if b==1: 
            wlen=QInputDialog.getInt(self,"Input Word Length","Give Word Length")
            search_sequence+="Search word length:{}".format(wlen)
            words=self.lexicon.word_length(wlen[0])
        elif b==2: 
            start_sequence=QInputDialog.getText(self,"Input Start Sequence","Give start sequence")
            search_sequence+="Search words starts with:{}".format(start_sequence)
            words=self.lexicon.starts_with(start_sequence[0])
        elif b==3: 
            end_sequence=QInputDialog.getText(self,"Input end Sequence","Give End Sequence")
            search_sequence+="Search words ends with:{}".format(end_sequence)
            words=self.lexicon.ends_with(end_sequence[0])
        elif b==4:
            contain_seq=QInputDialog.getText(self,"Input Contain sequence","Give contain sequence")
            rep_time=QInputDialog.getInt(self,"Repition Time","Give repetition time")
            search_sequence+="Search words contain sequence:{} {} times".format(contain_seq,rep_time)
            words=self.lexicon.contains(contain_seq[0],rep_time[0])
        elif b==5:
            rep_sequence=QInputDialog.getText(self,"Input Sequence","Give input sequence")
            search_sequence+="Search words contain sequence:{}".format(rep_sequence)
            words=self.lexicon.find(rep_sequence[0])
        
        ledit="="*5+" Lexicon "+"="*5+'\n'
        ledit+=search_sequence+"\n"
        ledit+="Words:{}\n".format(len(words))
        ledit+='---\n'
        ledit+="\n".join(words)
        self.textEdit.setText(ledit)

def main():
    ap=QApplication(sys.argv)
    f=Frame()
    f.show()
    ap.exec_()

if __name__=='__main__':
    main()