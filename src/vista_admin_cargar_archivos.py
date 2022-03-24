import os
import shutil

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.database import db
from src.database.modelos import *

class VistaAdminCargarArchivos(QDialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("src/vistas/VistaAdminCargarArchivos.ui",self)

        self.lista_areas = []
        self.lista_ind_bus = []
        self.ind_busqueda = {}

        self.texto = texto

        self.setWindowTitle("Administrador")

        self.label_nombre_empresa.setText(self.texto)

        #parte de los lineEdits
        self.lineEdit_tipo_documental.returnPressed.connect(self.guardar_datos)
        self.lineEdit_path.returnPressed.connect(self.guardar_datos)

        #llenado del comboBox
        self.id_empresa = db.session.query(Empresa.id).filter(Empresa.nombre_empresa == self.texto).first()

        self.areas = db.session.query(Area).filter(Area.id_empresa == self.id_empresa[0]).all()
        for datos in self.areas:
            self.lista_areas.append(str(datos))

        self.comboBox_area.addItems(self.lista_areas)

        #parte del path de cargar archivos
        self.pushButton_cargar_archivos.clicked.connect(self.cargar_path)

        #parte de agregar índices de búsqueda
        self.lineEdit_i_b.returnPressed.connect(self.agregar_i_b)
        self.pushButton_agregar_i_b.clicked.connect(self.agregar_i_b)

        #parte de guaradr
        self.pushButton_guardar_datos.clicked.connect(self.guardar_datos)
        
    def cargar_path(self):
        self.path = QFileDialog.getExistingDirectory(self,'Buscar directorio',QDir.homePath())
        if self.path:
            self.lineEdit_path.setText(self.path)

    def agregar_i_b(self):
        i_b = QStringListModel()
        ind_bus = self.lineEdit_i_b.text()
        self.lista_ind_bus.append(ind_bus)
        i_b.setStringList(self.lista_ind_bus)
        self.listView_i_b.setModel(i_b)

    def guardar_datos(self):
        try:
            tipo_doc =  self.lineEdit_tipo_documental.text()
            tp = TipoDoc(str(tipo_doc))
            db.session.add(tp)
            db.session.commit()

            area = self.comboBox_area.currentText()
            area_rel = db.session.query(Area).filter(Area.nombre_area == str(area),Area.id_empresa == self.id_empresa[0]).all()

            area_rel[0].tipo_doc += [tp]
            db.session.commit()

            for ib in self.lista_ind_bus:
                self.ind_busqueda[ib] = ""

            mapa_stringneado = str(self.ind_busqueda)

            list_archivos = os.listdir(self.path)
            
            path_ruta = os.getcwd()
            path_ruta_u = path_ruta.replace("\\","/")
            print(path_ruta_u)

            if(os.path.isdir('{}/Documentos/{}/{}/{}'.format(path_ruta,self.texto,area,tipo_doc))):
                mensaje = QMessageBox()
                mensaje.setText("El directorio ya existe")
                mensaje.setInformativeText("Por favor, asegúrese de cargar los archivos de manera correcta")
                mensaje.setWindowTitle("Error")
                mensaje.exec_()
            else:
                os.makedirs('{}/Documentos/{}/{}/{}'.format(path_ruta_u,self.texto,area,tipo_doc))

            for direc in list_archivos:
                shutil.copy("{}/{}".format(self.path,direc),'{}/Documentos/{}/{}/{}'.format(path_ruta_u,self.texto,area,tipo_doc))

            for archivo in list_archivos:
                indice_bus = IndiceBusqueda(archivo,mapa_stringneado,tp.id)
                db.session.add(indice_bus)
                db.session.commit()

            mensaje.setText("Tarea Realizada")
            mensaje.setInformativeText("La tarea ha sido cumplida. Se han guardado los archivos y las relaciones de manera satisfactoriamente")
            mensaje.setWindowTitle("Tarea completa")
            mensaje.exec_()
        except:
            mensaje = QMessageBox()
            mensaje.setText("ERROR")
            mensaje.setInformativeText("Ha ocurrido un error al momento de realizar la tarea")
            mensaje.setWindowTitle("Error")
            mensaje.exec_()


