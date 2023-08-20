#!/usr/bin/python3
# This App Made By Sina Meysami
# Github: https://github.com/mrprogrammer2938
# Aparat: https://aparat.com/v/DwfFk
#


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import pyttsx3 as px
import sys
px.init()
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("form.ui",self)
        self.setWindowTitle("Text To Sound")
        
        self.start_btn.clicked.connect(self.text_to_sound)
        
    def text_to_sound(self):
        text = self.text_line.text()
        print(text)
        px.speak(text)
        
def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
main()