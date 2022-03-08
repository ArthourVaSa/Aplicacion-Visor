from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtCore import Qt

class TableAreaModel(QAbstractTableModel):
    
    def __init__(self, data, parent = None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data)