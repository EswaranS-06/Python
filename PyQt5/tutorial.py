from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class mw(QMainWindow):
    
    def __init__(self, parent = ..., flags = ...):
        super(mw).__init__(parent, flags)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Heading")
        self.initUI
        
    
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello")
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Clicl me")
        self.b1.clicked.connect(self.c)
        
    def c(self):
        self.label.setText("clidd")            

def c():
    print("Hi")

def window():
    app = QApplication(sys.argv)
    win = mw()
    
    win.show()
    sys.exit(app.exec_())
    
window()