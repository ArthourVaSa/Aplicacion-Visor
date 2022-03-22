from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.database import db
from src.database.modelos import *

class VistaAdminArchivosUser(QDialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("src/vistas/VistaAdminArchivosUsuarios.ui",self)

        self.texto = texto

        self.setWindowTitle("Administrador")

        self.label.setText(self.texto)