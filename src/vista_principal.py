import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("src/vistas/VistaMain.ui", self)

        self.modelo = QFileSystemModel()
        self.modelo.setRootPath('')

        self.treeViewBuscador.setModel(self.modelo)

        self.actionCargar_Archivos.triggered.connect(self.abrir_pdf)

    def abrir_pdf(self):
        path, _ = QFileDialog.getOpenFileName(self, "Seleccione un Archivo", "", "pdf(*.pdf)")

        if not path:
            return
        if _.find("*.pdf"):
            return self.openPdf(path)
    
    def openPdf(self, path):
        self.VisualizadorPdf.clear()
        if not self.VisualizadorPdf.setControl("Adobe PDF Reader"):
            return QMessageBox.critical(self,"Error","No se pudo abrir el archivo Adobe PDF Reader")
        self.VisualizadorPdf.dynamicCall("LoadFile(const QString&)", path)

def main():
    print('Todo tranqui')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.showMaximized()
    main()
    sys.exit(app.exec_())