from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaAdminUser(QDialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaAdminUser.ui",self)

        self.lista_usuarios = []
        self.lista_areas = []

        self.texto = texto

        self.setWindowTitle("Administrador")

        self.label.setText(self.texto)

        #parte de definir
        self.id_empresa = db.session.query(Empresa.id).filter(Empresa.nombre_empresa == self.texto).first()
        self.usuarios = db.session.query(User).filter(User.rol_id == 3, User.empresa_id == self.id_empresa[0]).all()
        for data in self.usuarios:
            self.lista_usuarios.append(str(data))

        self.comboBox_usuarios.addItems(self.lista_usuarios)

        self.areas = db.session.query(Area).filter(Area.id_empresa == self.id_empresa[0]).all()
        for datos in self.areas:
            self.lista_areas.append(str(datos))

        self.comboBox_areas.addItems(self.lista_areas)

        self.pushButton_def_relacion.clicked.connect(self.definir_relacion)

        #parte tabla
        relacion = db.session.query(Area).filter(Area.usuarios.any(User.username == 'Miqueas')).all()
        for dato in relacion:
            print(dato)

    def definir_relacion(self):

        try:
            area = self.comboBox_areas.currentText()
            usuario = self.comboBox_usuarios.currentText()

            user_rel = db.session.query(User).filter(User.username == str(usuario), User.empresa_id == self.id_empresa[0]).all()
            area_rel = db.session.query(Area).filter(Area.nombre_area == str(area),Area.id_empresa == self.id_empresa[0]).all()

            area_rel[0].usuarios += [user_rel[0]]

            area_rel[0].usuarios 

            db.session.commit()

            mensaje = QMessageBox()
            mensaje.setText("Relación Realizada")
            mensaje.setInformativeText("La tarea ha sido cumplida. Se ha aplicado la relación satisfactoriamente")
            mensaje.setWindowTitle("Tarea completa")
            mensaje.exec_()
        except:
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Ha ocurrido un error al editar el área para la empresa")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_() 


        