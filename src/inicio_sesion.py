# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioSesion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vista_admin_inicio import *
from vista_super_inicio import VistaSuperInicio

from database import db
from database.modelos import *

import time

def validacion_mensaje(mensaje, informacion):

    msg = QMessageBox()

    msg.setIcon(QMessageBox.Information)

    msg.setText(mensaje)
    msg.setInformativeText(informacion)
    msg.setWindowTitle("Valiación")
    msg.setStandardButtons(QMessageBox.Ok)

    msg.exec_()
    return

# Clase para definir el incio de sesion
class Ui_dlgInicioSesionVista(object):

    # Define el método setupUi
    def setupUi(self, dlgInicioSesionVista):

        # Coloca el nombre del objeto
        dlgInicioSesionVista.setObjectName("dlgInicioSesionVista")

        # Establece el tamaño del dialog    
        dlgInicioSesionVista.resize(398, 300)

        # Definimos el GroupBox donde irán encerrados otros widgets
        self.gbUsuarioContrasea = QtWidgets.QGroupBox(dlgInicioSesionVista)

        # Definimos el tamaño y posición del GroupBox
        self.gbUsuarioContrasea.setGeometry(QtCore.QRect(10, 10, 371, 141))

        # Colocamos el nombre de la clase del GroupBox
        self.gbUsuarioContrasea.setObjectName("gbUsuarioContrasea")

        # Creamos el primer label del Usuario, encerrando en el GroupBox
        self.lbUsuario = QtWidgets.QLabel(self.gbUsuarioContrasea)

        # Definimos el tamaño y posicion del Label
        self.lbUsuario.setGeometry(QtCore.QRect(30, 30, 81, 21))

        # Creamos la clase parad definir la fuente y definimos las demás propiedades
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        # Definimos la fuente al label del Usuario, Le damos el nombre al objeto
        self.lbUsuario.setFont(font)
        self.lbUsuario.setObjectName("lbUsuario")

        """
        Creamos el label Password y le damos tamaño y posición a este. Dándole la misma fuente
        y definiendo el nombre del objeto.
        """
        self.lbPassword = QtWidgets.QLabel(self.gbUsuarioContrasea)
        self.lbPassword.setGeometry(QtCore.QRect(30, 90, 111, 21))
        self.lbPassword.setFont(font)
        self.lbPassword.setObjectName("lbPassword")

        # Definimos el LineEdit del Usuario (Caja de Texto). Seguidamente:
        """
        Denimos nuevamente el tamaño dado que el tipo de letra que usaremos es la que
        trae por defecto. Luego le atribuimos cada cosa que necesitamos y finalmente
        le ponemos el nombre de nuestro Objeto.
        """
        self.leUsuario = QtWidgets.QLineEdit(self.gbUsuarioContrasea)
        self.leUsuario.setGeometry(QtCore.QRect(170, 30, 181, 21))
        fontLineEdit = QtGui.QFont()
        fontLineEdit.setFamily("Consolas")
        self.leUsuario.setFont(fontLineEdit)
        self.leUsuario.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.leUsuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leUsuario.setClearButtonEnabled(True)
        self.leUsuario.setObjectName("leUsuario")
        self.leUsuario.returnPressed.connect(self.controlarFoco)

        # Definimos el LineEdit del password, aplicando la fuente para los fontLineEdit
        # Y asi agregando cada función a utilizafr y finalmente
        # Le agreamos el nombre del Objeto
        self.lePassword = QtWidgets.QLineEdit(self.gbUsuarioContrasea)
        self.lePassword.setGeometry(QtCore.QRect(170, 90, 181, 21))
        self.lePassword.setFont(fontLineEdit)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lePassword.setClearButtonEnabled(True)
        self.lePassword.setObjectName("lePassword")
        self.lePassword.returnPressed.connect(self.controlarFoco)

        # Definimos el GroupBox de los botones y luego le damos su tamaño y posición
        # Tmabién le quitamos el titutlo y le damos un nombre al objeto
        self.gbBotonesAcpCanc = QtWidgets.QGroupBox(dlgInicioSesionVista)
        self.gbBotonesAcpCanc.setGeometry(QtCore.QRect(10, 160, 371, 121))
        self.gbBotonesAcpCanc.setTitle("")
        self.gbBotonesAcpCanc.setObjectName("gbBotonesAcpCanc")

        # Definimos el botón aceptar par luego atribuirle su tamña y posición.
        # Luego definimos el icono de la imagen y finalmente le damos el nombre del objeto
        self.pbAceptar = QtWidgets.QPushButton(self.gbBotonesAcpCanc)
        self.pbAceptar.setGeometry(QtCore.QRect(20, 40, 111, 31))
        self.pbAceptar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("archivos/src/img/aceptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon)
        self.pbAceptar.setObjectName("pbAceptar")
        # self.pbAceptar.setAutoDefault(False)
        # self.pbAceptar.setDefault(False)
        self.pbAceptar.clicked.connect(lambda: self.proceso_aceptar(dlgInicioSesionVista))

        # Definimos el botón cancelar par luego atribuirle su tamña y posición.
        # Luego definimos el icono de la imagen y finalmente le damos el nombre del objeto
        self.pbCancelar = QtWidgets.QPushButton(self.gbBotonesAcpCanc)
        self.pbCancelar.setGeometry(QtCore.QRect(240, 40, 111, 31))
        self.pbCancelar.setFont(font)
        icon.addPixmap(QtGui.QPixmap("archivos/src/img/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelar.setIcon(icon)
        # self.pbCancelar.setAutoDefault(False)
        self.pbCancelar.setObjectName("pbCancelar")

        self.retranslateUi(dlgInicioSesionVista)
        QtCore.QMetaObject.connectSlotsByName(dlgInicioSesionVista)

    def retranslateUi(self, dlgInicioSesionVista):
        _translate = QtCore.QCoreApplication.translate
        dlgInicioSesionVista.setWindowTitle(_translate("dlgInicioSesionVista", "Inicio de Sesión"))
        self.gbUsuarioContrasea.setTitle(_translate("dlgInicioSesionVista", "Usuario y Contraseña"))
        self.lbUsuario.setText(_translate("dlgInicioSesionVista", "Usuario:"))
        self.lbPassword.setText(_translate("dlgInicioSesionVista", "Contraseña:"))
        self.leUsuario.setPlaceholderText(_translate("dlgInicioSesionVista", "Ingrese su usuario"))
        self.lePassword.setPlaceholderText(_translate("dlgInicioSesionVista", "Ingrese su contraseña"))
        self.pbAceptar.setText(_translate("dlgInicioSesionVista", "Aceptar"))
        self.pbCancelar.setText(_translate("dlgInicioSesionVista", "Cancelar"))

    def controlarFoco(self):
        print("Has presionado enter")

        if (self.leUsuario.hasFocus()):
            print("Foco a password")
            self.lePassword.setFocus()
        else:
            print("Foco a aceptar")
            self.pbAceptar.setFocus()

    def proceso_aceptar(self, dlgInicioSesionVista):
        if (self.pbAceptar.hasFocus()):
            self.validar_datos(dlgInicioSesionVista)
    
    def validar_datos(self, dlgInicioSesionVista):
        mensaje = ""

        if (len(self.leUsuario.text())==0):
            mensaje = "El Usuario\n"
            self.leUsuario.setFocus()
        
        if (len(self.lePassword.text())==0):
            if (mensaje==0):
                self.lePassword.setFocus()

            mensaje = mensaje + "La Contraseña"

        if (len(mensaje)>0):
            mensaje = "Revise los siguientes datos:\n" + mensaje

            validacion_mensaje(mensaje, "El Usuario y La Contraseña no pueden quedar vacíos")

            return False
        else:
            validacion_mensaje("Los datos se han introducido correctamente", "La aplicación intentara el acceso")

            nombre = self.leUsuario.text()
            password = self.lePassword.text()

            rol = db.session.query(User.rol_id).filter(User.username == nombre, User.password == password).first()
            nombre_rol = db.session.query(Rol.rol_nombre).filter(Rol.id == rol[0]).first()
            
            if(nombre_rol[0] == "SuperUsuario"):
                self.go_to_super_inicio(dlgInicioSesionVista)
            elif (nombre_rol[0] == "Administrador"):
                self.go_to_admin_area(dlgInicioSesionVista,nombre,password)

            return True

    def go_to_super_inicio(self,dlgInicioSesionVista):
        # QtWidgets.QDialog.__init__(QtWidgets.QDialog)
        self.ir_super_inicio = VistaSuperInicio()
        self.ir_super_inicio.__init__()

        time.sleep(3)
        dlgInicioSesionVista.close()

        self.ir_super_inicio.show()

    def go_to_admin_area(self, dlgInicioSesionVista, name, password):
        self.empresa_id = db.session.query(User.empresa_id).filter(User.username == name, User.password == password).first()
        self.nombre_empresa = db.session.query(Empresa.nombre_empresa).filter(Empresa.id == self.empresa_id[0]).first()
        texto = str(self.nombre_empresa[0])
        self.ir_super_inicio = VistaAdminInicio(texto)
        # self.ir_super_inicio.__init__(self.nombre_empresa[0])

        time.sleep(3)
        dlgInicioSesionVista.close()

        self.ir_super_inicio.show()

    def enviar_empresa(self):
        return self.nueva_empresa
         


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    dlgInicioSesionVista = QtWidgets.QDialog()
    ui = Ui_dlgInicioSesionVista()
    ui.setupUi(dlgInicioSesionVista)
    dlgInicioSesionVista.show()
    sys.exit(app.exec_())
