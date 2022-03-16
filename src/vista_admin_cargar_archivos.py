from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaAdminCargarArchivos(QDialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaAdminCargarArchivos.ui",self)

        self.texto = texto

        self.setWindowTitle("Administrador")

        self.label_nombre_empresa.setText(self.texto)