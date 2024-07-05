import sys
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

def main():
    #Create application
    app = QApplication(sys.argv)
    #Connect to database before windows are created
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    #Create main window if connection succeeded
    win = Window()
    win.show()
    #Run application
    sys.exit(app.exec_())