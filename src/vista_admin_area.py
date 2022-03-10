from pyexpat import model
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaAdminArea(QDialog):

    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaAdminArea.ui",self)

        self.texto = texto

        self.setWindowTitle("Administrador")

        self.label_empresa.setText(self.texto)

        #agregar area
        self.lineEdit_nombre_area.returnPressed.connect(self.agregar_area)
        self.pushButton_agregar_area.clicked.connect(self.agregar_area)

    def agregar_area(self):
        nombre_area = self.lineEdit_nombre_area.text()

        if (len(nombre_area) == 0):
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Por favor inserte el nombre del área a crear")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()
        else:
            pass

               

def main():
    app = QApplication(sys.argv)
    window = VistaAdminArea()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()