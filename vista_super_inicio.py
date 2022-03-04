import sys
from tkinter import SEL
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from vista_superuser import *
from vista_super_empresa import *
from inicio_sesion import Ui_dlgInicioSesionVista

import time

class VistaSuperInicio(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaSuperInicio.ui",self)

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

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Even - Slot',"Realmente desea cerrar la aplicación",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)   

        if(reply == QMessageBox.Yes):
            time.sleep(2)
            event.accept()
        else:
            event.ignore()

    
    def volver_inicio_sesion(self):
        dlgInicioSesionVista = QDialog()
        ui = Ui_dlgInicioSesionVista()
        ui.setupUi(dlgInicioSesionVista)
        dlgInicioSesionVista.show()

def main():
    app = QApplication(sys.argv)
    window = VistaSuperInicio()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
