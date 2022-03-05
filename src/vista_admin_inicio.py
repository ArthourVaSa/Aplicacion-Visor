import sys
from tkinter import SEL
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from vista_admin_area import *

import time

class VistaAdminInicio(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("src/vistas/VistaAdminInicio.ui",self)

        self.setWindowTitle("Inicio Administrador")

        self.pushButton_def_area_empresa.clicked.connect(self.go_to_def_area)

    def go_to_def_area(self):
        QDialog.__init__(self)
        self.ir_super_user = VistaAdminArea()
        self.ir_super_user.__init__()

        self.ir_super_user.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Even - Slot',"Realmente desea cerrar la aplicación",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)   

        if(reply == QMessageBox.Yes):
            time.sleep(2)
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    window = VistaAdminInicio()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()