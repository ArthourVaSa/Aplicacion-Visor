import sys
import os
import ast

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database.modelos import *

from database import db

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("vistas/VistaMain.ui", self)

        self.nombre_carpeta_tipo_doc = db.session.query(TipoDoc.tipo_doc).filter_by(tipo_doc="factura").first()
        print(self.nombre_carpeta_tipo_doc)

        # os.makedirs("D:/Arthour/Trabajos/Nexuzz/Archivos/documentos/"+self.nombre_carpeta_tipo_doc[0])

        self.modelo = QFileSystemModel(self)
        self.modelo.setRootPath("D:/Arthour/Trabajos/Nexuzz/Archivos/documentos/")
        print(self.modelo)

        self.treeViewBuscador.setModel(self.modelo)
        self.treeViewBuscador.setRootIndex(self.modelo.index("D:/Arthour/Trabajos/Nexuzz/Archivos/documentos/"))

        self.lista_indices = []
        self.nombre_i_b = db.session.query(IndiceBusqueda.nombre_archivo).filter_by(nombre_archivo="CV.pdf").first()
        self.lista_indices.append("nombre")
        self.nombre_i_b_mapa = db.session.query(IndiceBusqueda.indice_busqueda).filter(TipoDoc.id_indice_busqueda == IndiceBusqueda.id).first()
        mapa_indices = ast.literal_eval(self.nombre_i_b_mapa[0])
        self.counter = 1
        self.row = 0
        for k in mapa_indices.keys():
            self.counter += 1
            self.lista_indices.append(k)
        self.tableWidgetLlenado.setColumnCount(self.counter)
        self.tableWidgetLlenado.setHorizontalHeaderLabels(self.lista_indices)
        for value in mapa_indices.values():
            self.tableWidgetLlenado.insertRow(self.row)
            nombre = QTableWidgetItem(str(self.nombre_i_b[0]))
            # ruc = QTableWidgetItem(value))
            # fecha
            # monto
            # sede
            self.tableWidgetLlenado.setItem(self.row,0,nombre)


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