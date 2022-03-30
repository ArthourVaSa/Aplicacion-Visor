import ast
import os
from re import T
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
        self.lista_items = ['id','nombre']

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
        self.treeViewBuscador.setRootIndex(self.modelo.index('{}/Documentos/{}'.format(path_ruta_local,self.empresa)))

        #parte del tablewidget  

    def jalar_path(self, Qmodelidx):
        print(self.modelo.filePath(Qmodelidx))
        self.nombre_tipodoc = self.modelo.fileName(Qmodelidx)
        self.parte_table(self.nombre_tipodoc)
        
    def parte_table(self, nombre):
        tipo_doc = db.session.query(TipoDoc.id).filter(TipoDoc.tipo_doc == nombre).first()
        indices_bus = db.session.query(IndiceBusqueda).filter(IndiceBusqueda.id_tipo_doc == tipo_doc[0]).all()

        row = 0
        for data in indices_bus:
            self.tableWidget_Llenado.insertRow(row)
            id = QTableWidgetItem(str(data.id))
            nombre = QTableWidgetItem(str(data.nombre_archivo))
            self.mapa = ast.literal_eval(data.indice_busqueda)
            self.tableWidget_Llenado.setItem(row,0,id)
            self.tableWidget_Llenado.setItem(row,1,nombre)
            row = row + 1
        
        for k in self.mapa.keys():
            self.lista_items.append(k)

        self.tableWidget_Llenado.setColumnCount(len(self.lista_items))    
        self.tableWidget_Llenado.setHorizontalHeaderLabels(self.lista_items) 

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

    def go_to_admin_area(self):
        self.empresa_id = db.session.query(User.empresa_id).filter(User.username == self.nombre_usuario).first()
        print(self.empresa_id[0])
        self.nombre_empresa = db.session.query(Empresa.nombre_empresa).filter(Empresa.id == self.empresa_id[0]).first()
        texto = str(self.nombre_empresa[0])
        self.ir_super_inicio = VistaAdminInicio(texto)

        self.ir_super_inicio.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Even - Slot',"Realmente desea cerrar la aplicación",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)   

        if(reply == QMessageBox.Yes):
            time.sleep(2)
            event.accept()
        else:
            event.ignore()