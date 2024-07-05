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
