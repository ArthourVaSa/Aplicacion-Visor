from ast import Lambda
import sys
from tkinter import SEL
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.vista_admin_archivos_usuarios import *
from src.vista_admin_cargar_archivos import *
from src.vista_admin_user import *
from src.vista_admin_area import *

import time

class VistaAdminInicio(QDialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("src/vistas/VistaAdminInicio.ui",self)

        self.texto_pasado = texto

        self.setWindowTitle("Inicio Administrador")

        self.label_nombre_empresa.setText(self.texto_pasado)

        self.pushButton_def_area_empresa.clicked.connect(self.go_to_def_area)

        self.pushButton_def_usuario_area.clicked.connect(self.go_to_def_user_area)
        
        self.pushButton_archivos_area.clicked.connect(self.go_to_cargar_archivos)

        self.pushButton_archivos_usuarios.clicked.connect(self.go_to_archivos_user)

    def go_to_def_area(self):
        QDialog.__init__(self)
        self.ir_super_user = VistaAdminArea(self.texto_pasado)

        self.ir_super_user.show()

    def go_to_def_user_area(self):
        QDialog.__init__(self)
        self.ir_user_area = VistaAdminUser(self.texto_pasado)
        self.ir_user_area.show()

    def go_to_cargar_archivos(self):
        QDialog.__init__(self)
        self.ir_cargar_archivos = VistaAdminCargarArchivos(self.texto_pasado)
        self.ir_cargar_archivos.show()

    def go_to_archivos_user(self):
        QDialog.__init__(self)
        self.ir_archivos_user = VistaAdminArchivosUser(self.texto_pasado)
        self.ir_archivos_user.show()