import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.vista_admin_inicio import VistaAdminInicio
from src.vista_super_inicio import VistaSuperInicio

from src.database import db
from src.database.modelos import *

import time

class VentanaPrincipal(QMainWindow):
    def __init__(self, empresa, nombre_usuario):
        QMainWindow.__init__(self)
        uic.loadUi("src/vistas/VistaMain.ui", self)

        self.empresa = empresa
        self.nombre_usuario = nombre_usuario

        #parte actions
        rol = db.session.query(User.rol_id).filter(User.username == self.nombre_usuario).first()
        nombre_rol = db.session.query(Rol.rol_nombre).filter(Rol.id == rol[0]).first()
            
        if(nombre_rol[0] == "SuperUsuario"):
            self.actionAdministrador.setEnabled(False)
        elif (nombre_rol[0] == "Administrador"):
            self.actionSuperUsuario.setEnabled(False)
        elif (nombre_rol[0] == "Usuario"):
            self.actionAdministrador.setEnabled(False)
            self.actionSuperUsuario.setEnabled(False)
            
        self.actionCargar_Archivos.triggered.connect(self.abrir_pdf)
        self.actionAdministrador.triggered.connect(self.go_to_admin_area)
        self.actionSuperUsuario.triggered.connect(self.go_to_super_inicio)

        #parte del treeview
        path_local = os.getcwd()
        path_ruta_local = path_local.replace("\\","/")
        self.treeViewBuscador.doubleClicked.connect(self.jalar_path)
        self.modelo = QDirModel()
        self.treeViewBuscador.setModel(self.modelo)
        self.treeViewBuscador.setRootIndex(self.modelo.index('{}/Documentos/'.format(path_ruta_local)))

    def jalar_path(self, Qmodelidx):
        print(self.modelo.filePath(Qmodelidx))

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

    def go_to_super_inicio(self):
        self.ir_super_inicio = VistaSuperInicio()
        self.ir_super_inicio.__init__()

        self.ir_super_inicio.show()

    def go_to_admin_area(self, name):
        self.empresa_id = db.session.query(User.empresa_id).filter(User.username == name).first()
        self.nombre_empresa = db.session.query(Empresa.nombre_empresa).filter(Empresa.id == self.empresa_id[0]).first()
        texto = str(self.nombre_empresa[0])
        self.ir_super_inicio = VistaAdminInicio(texto)

        self.ir_super_inicio.show()

def main():
    print('Todo tranqui')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.showMaximized()
    main()
    sys.exit(app.exec_())