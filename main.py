import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

sys.path.append("..")

from archivos.widgets.archivos import VisorDatos

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1340,720)
        self.setWindowTitle("Primera App")
        
        self.layout_general = QHBoxLayout()
        self.widget_general = QWidget(self)
        self.widget_general.setGeometry(0,0,300,720)
        
        self.widget_buscador = QWidget(self)
        self.vista = VisorDatos()
        self.widget_buscador.setLayout(self.vista.layout_total)
        
        self.layout_general.addWidget(self.widget_buscador)
        self.widget_general.setLayout(self.layout_general)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())