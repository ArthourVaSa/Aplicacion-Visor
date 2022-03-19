from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaAdminCargarArchivos(QDialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaAdminCargarArchivos.ui",self)

        self.lista_areas = []
        self.lista_ind_bus = []

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
        
    def cargar_path(self):
        path = QFileDialog.getExistingDirectory(self,'Buscar directorio',QDir.homePath())
        if path:
            self.lineEdit_path.setText(path)

    def agregar_i_b(self):
        i_b = QStringListModel()
        ind_bus = self.lineEdit_i_b.text()
        self.lista_ind_bus.append(ind_bus)
        i_b.setStringList(self.lista_ind_bus)
        self.listView_i_b.setModel(i_b)

    def guardar_datos(self):
        tipo_doc =  self.lineEdit_tipo_documental.text()
        tp = TipoDoc(str(tipo_doc))
        db.session.add(tp)
        db.session.commit(tp)

        area = self.comboBox_area.currentText()
        area_rel = db.session.query(Area).filter(Area.nombre_area == str(area),Area.id_empresa == self.id_empresa[0]).all()

        area_rel[0].tipo_doc += [tp]

        
