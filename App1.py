from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow): # QMainWindow
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        
        self.setWindowTitle('Aplicacion1')

        button = QPushButton('Push me if you dare!') # Widget "button"
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        
        self.setMinimumSize(400,300)
        self.setMaximumSize(1200,900)
        
        self.setCentralWidget(button)
    
    def button_clicked(self): # Definition of what happens when we click
        print("Button was clicked!") # Our signal

app= QApplication(sys.argv) # QApplication, this is the "Event Handler", we only need one per App
window = MainWindow()

window.show()

app.exec_() # This executes the app when we run the program