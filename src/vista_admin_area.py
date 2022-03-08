import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaAdminArea(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("src/vistas/VistaAdminArea.ui",self)

        self.setWindowTitle("Administrador")

        #agregar area
        self.pushButton_agregar_area.clicked.connect(self.go_to_add_area)

    def go_to_add_area(self):
        pass

               

def main():
    app = QApplication(sys.argv)
    window = VistaAdminArea()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()