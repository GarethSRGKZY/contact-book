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
        headers = ("ID", "Name", "Job", "Phone No.", "Email")
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

    def deleteContact(self, row):
        """Delete a contact from the database"""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()
    
    def clearContacts(self):
        """Delete all contacts from the database"""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

    def searchContacts(self, searchText):
        """Search for contacts that match the given search text"""
        filterString = (
            f"name LIKE '%{searchText}%' OR "
            f"job LIKE '%{searchText}%' OR "
            f"phone LIKE '%{searchText}%' OR "
            f"email LIKE '%{searchText}%'"
        )
        self.model.setFilter(filterString)
        self.model.select()