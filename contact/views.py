from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
)

from .model import ContactsModel

class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Contacts")
        self.resize(700, 550)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        # Create table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create buttons
        self.addButton = QPushButton("Add Contact")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete Contact")
        self.clearAllButton = QPushButton("Clear All")

        # GUI Layout
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
    
    def openAddDialog(self):
        """Open Add Contact Dialog"""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()

class AddDialog(QDialog):
    """Add contact dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()  # Corrected the instantiation
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup GUI for Add Contact dialog"""
        # Create line edits for data fields
        self.nameField = QLineEdit()  # Corrected the variable name
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()  # Corrected the variable name
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()  # Corrected the variable name
        self.emailField.setObjectName("Email")
        # Layout data fields
        layout = QFormLayout()
        layout.addRow("Name", self.nameField)
        layout.addRow("Job", self.jobField)
        layout.addRow("Email", self.emailField)
        self.layout.addLayout(layout)
        # Add standard buttons to the dialog and connect
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)
    
    def accept(self):
        """Accepts the data provided through the dialog"""
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField):  # Corrected the variable names
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error",
                    f"You need to provide a contact's {field.objectName()}",
                )
                self.data = None  # Data Reset
                return
            
            self.data.append(field.text())
        
        super().accept()
