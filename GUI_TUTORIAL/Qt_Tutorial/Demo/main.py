import window as w
import PyQt5.QtWidgets as qt

def main():
    x =qt.QApplication([])
    win=w.App()
    win.show()
    return x.exec()

if __name__=="__main__":
   main()