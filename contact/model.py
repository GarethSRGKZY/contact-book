from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and Set Up Model"""
        model = QSqlTableModel()
        model.setTable("contacts")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        headers = ("ID", "Name", "Job", "Email")
        for columnIndex, header in enumerate(headers):
            model.setHeaderData(columnIndex, Qt.Horizontal, header)
        return model
    
    def addContact(self, data):
        """Add a new contact to the database"""
        rows = self.model.rowCount()
        self.model.insertRow(rows)
        for column, field in enumerate(data, start=1):
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()
