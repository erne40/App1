from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow): # QMainWindow
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        
        self.setWindowTitle('Aplicacion1')

        label= QLabel('Primer App') # Widget
        label.setAlignment(Qt.AlignCenter)
        
        self.setMinimumSize(400,300)
        self.setMaximumSize(1200,900)
        # self.setFixedSize(QSize(400, 300)) # Fix window size to 400x300 pixels
        
        self.setCentralWidget(label)

app= QApplication(sys.argv) # QApplication, this is the "Event Handler", we only need one per App
window = MainWindow()

window.show()

app.exec_() # This executes the app when we run the program