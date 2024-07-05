import sys
from PyQt5.QtWidgets import QApplication
from .views import Window

def main():
    #Create application
    app = QApplication(sys.argv)
    #Create main window
    win = Window()
    win.show()
    #Run application
    sys.exit(app.exec())