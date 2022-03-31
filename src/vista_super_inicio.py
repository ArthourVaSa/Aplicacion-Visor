import sys
from tkinter import SEL
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.vista_superuser import *
from src.vista_super_empresa import *
# from src.inicio_sesion import *

import time

class VistaSuperInicio(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("src/vistas/VistaSuperInicio.ui",self)

        self.pushButton_funciones_usuarios.clicked.connect(self.go_to_usuario)
        self.pushButton_funciones_empresas.clicked.connect(self.go_to_empresa)

    def go_to_usuario(self):
        QDialog.__init__(self)
        self.ir_super_user = VistaSuperUser()
        self.ir_super_user.__init__()

        self.ir_super_user.show()

    def go_to_empresa(self):
        QDialog.__init__(self)
        self.ir_super_empresa = VistaSuperEmpresa()
        self.ir_super_empresa.__init__()

        self.ir_super_empresa.show()
