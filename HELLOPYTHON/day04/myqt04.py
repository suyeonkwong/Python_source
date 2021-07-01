import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

 
form_class = uic.loadUiType('myqt04.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.my_clicked)
    
        
    def my_clicked(self):
       a = int(self.le1.text())
       b = int(self.le2.text())
       c = a + b
       self.le3.setText(str(c))

 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

