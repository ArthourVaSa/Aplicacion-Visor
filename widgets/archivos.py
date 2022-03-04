import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class VisorDatos(QWidget):
    def __init__(self):
        super().__init__()

        self.modelo = QFileSystemModel()
        self.modelo.setRootPath('')

        self.vista = QTreeView()
        self.vista.setModel(self.modelo)
        self.vista.setColumnWidth(200,250)
        self.vista.setAlternatingRowColors(True)
        self.vista.doubleClicked.connect(self.conseguir_directorio)

        self.layout_total = QVBoxLayout()
        self.layout_total.addWidget(self.vista)

    def conseguir_directorio(self, model):
        print(self.modelo.filePath(model))
