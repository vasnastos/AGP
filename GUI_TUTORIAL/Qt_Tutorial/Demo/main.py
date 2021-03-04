import window as w
import PySide6.QtWidgets as qt

def main():
    x =qt.QApplication()
    win=w.App()
    win.show()
    return x.exec_()

if __name__=="__main__":
   main()