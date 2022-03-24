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

        #parte de la relación
        self.id_empresa = db.session.query(Empresa.id).filter(Empresa.nombre_empresa == self.texto).first()
        self.tipo_doc = db.session.query(TipoDoc.tipo_doc).filter(Empresa.id == Area.id_empresa, )