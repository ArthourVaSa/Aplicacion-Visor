import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.inicio_sesion import *

class App(QApplication):

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        #conectando todo
        self.dlgInicioSesionVista = QDialog()
        self.ui = Ui_dlgInicioSesionVista()
        self.ui.setupUi(self.dlgInicioSesionVista)
        self.dlgInicioSesionVista.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())