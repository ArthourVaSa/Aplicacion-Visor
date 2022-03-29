from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.database import db
from src.database.modelos import *

class VistaAdminArchivosUser(QDialog):
    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("src/vistas/VistaAdminArchivosUsuarios.ui",self)

        self.lista_areas = []
        self.lista_usuario = []
        self.texto = texto

        self.setWindowTitle("Administrador")

        self.label.setText(self.texto)

        #parte de la relación
        self.id_empresa = db.session.query(Empresa.id).filter(Empresa.nombre_empresa == self.texto).first()
        self.areas = db.session.query(Area).filter(Area.id_empresa == self.id_empresa[0]).all()
        for datos in self.areas:
            self.lista_areas.append(str(datos))
        
        self.comboBox_area.addItems(self.lista_areas)
        self.comboBox_area.activated[str].connect(self.onChanged)

        self.usuarios = db.session.query(User).filter(User.empresa_id == self.id_empresa[0]).all()
        for user in self.usuarios:
            self.lista_usuario.append(str(user))

        self.comboBox_user.addItems(self.lista_usuario)

        #botones
        self.pushButton_guardar.clicked.connect(self.guardar_relacion)

    def onChanged(self):
        self.comboBox_tipo_doc.clear()
        area = self.comboBox_area.currentText()
        
        relacion = db.session.query(TipoDoc.tipo_doc).filter(TipoDoc.area.any(Area.nombre_area == str(area))).all()
        if(len(relacion) == 0):
            mensaje = QMessageBox()
            mensaje.setText("ERROR")
            mensaje.setInformativeText("No existe este tipo documental en el área.")
            mensaje.setWindowTitle("Error")
            mensaje.exec_()
        else:
            self.comboBox_tipo_doc.addItems(relacion[0])

    def guardar_relacion(self):
        try:
            tipo_d = self.comboBox_tipo_doc.currentText()
            usuario = self.comboBox_user.currentText()

            q_tipo_d = db.session.query(TipoDoc).filter(TipoDoc.tipo_doc == str(tipo_d)).all()
            q_usuario = db.session.query(User).filter(User.username == str(usuario), User.empresa_id == self.id_empresa[0]).all()

            q_usuario[0].tipo_documental += [q_tipo_d[0]]
            db.session.commit()

            mensaje.setText("Tarea Realizada")
            mensaje.setInformativeText("La tarea ha sido cumplida. Se han guardado las relaciones de manera satisfactoriamente")
            mensaje.setWindowTitle("Tarea completa")
            mensaje.exec_()
        except:
            mensaje = QMessageBox()
            mensaje.setText("ERROR")
            mensaje.setInformativeText("Ha ocurrido un error al momento de realizar la tarea")
            mensaje.setWindowTitle("Error")
            mensaje.exec_()