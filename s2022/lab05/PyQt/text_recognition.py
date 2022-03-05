import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QTextCharFormat, QTextCursor
from PyQt5.Qt import QFile,QFileDialog,QTextStream,QIODevice
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                                QToolBar, QLineEdit, QPushButton, QColorDialog, QHBoxLayout, QWidget,QMenuBar,QMenu,QAction,QFileDialog)


class TextEdit(QMainWindow):
    def menu(self):
        menu=QMenu("EDIT",self)
        act1=QAction("Import",self)
        act2=QAction("Save",self)
        act1.triggered.connect(self.add_text)
        act2.triggered.connect(self.save_mode)
        menu.addAction(act1)
        menu.addAction(act2)
        self.menuBar().addMenu(menu)


    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.setWindowTitle("Text Recognition App")
        self.menu()
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        widget = QWidget(self)
        vb = QHBoxLayout(widget)
        vb.setContentsMargins(0, 0, 0, 0)
        self.findText = QLineEdit(self)
        self.findText.setFixedWidth(int(0.45 * self.width()))
        findBtn = QPushButton('Search', self)
        findBtn.setFixedWidth(int(0.23*self.width()))
        findBtn.setStyleSheet(
            """
            QPushButton{
                color:white;
                background-color:#33568f;
                font-weight:bold;
                font-size:14px;
            }
            """
        )
        findBtn.clicked.connect(self.highlight)
        vb.addWidget(self.findText)
        vb.addWidget(findBtn)

        tb = QToolBar(self)
        tb.addWidget(widget)
        self.addToolBar(tb)
        self.textEdit.setStyleSheet(
            """
            QTextEdit
            {
                font-size:16px;
                font-weight:bold;
            }
            """
        )
        self.textEdit.setReadOnly(True)

    def setText(self, text):
        self.textEdit.setPlainText(text)

    def highlight(self):
        text = self.findText.text()  
        if not text:
            return

        col = QColorDialog.getColor(self.textEdit.textColor(), self)
        if not col.isValid():
            return

        cursor = self.textEdit.textCursor()
        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(QTextCharFormat())
        cursor.clearSelection()
        self.textEdit.setTextCursor(cursor)

        fmt = QTextCharFormat()
        fmt.setForeground(col)

        expression = QRegExp(text)
        self.textEdit.moveCursor(QTextCursor.Start)
        cursor = self.textEdit.textCursor()

        pos = 0
        index = expression.indexIn(self.textEdit.toPlainText(), pos)
        while index >= 0:
            cursor.setPosition(index)
            cursor.movePosition(QTextCursor.Right,
                                QTextCursor.KeepAnchor, len(text))
            cursor.mergeCharFormat(fmt)
            pos = index + expression.matchedLength()
            index = expression.indexIn(self.textEdit.toPlainText(), pos)
    
    def add_text(self):
        self.textEdit.setStyleSheet(
            """
            QTextEdit
            {
                color:black;
                font-size:16px;
                font-weight:bold;
            }
            """
        )
        fn=QFileDialog.getOpenFileName(self,'Select input file','.','*.txt')
        if len(fn[0])==0: return
        fp=QFile(fn[0])
        fp.open(QIODevice.ReadOnly)
        stream=QTextStream(fp)
        line=''
        while not stream.atEnd():
            line+=stream.readLine()+"\n"
        fp.close()
        self.textEdit.setText(line)
    
    def save_mode(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    textEdit = TextEdit()
    textEdit.resize(800, 600)
    textEdit.show()

    sys.exit(app.exec_())