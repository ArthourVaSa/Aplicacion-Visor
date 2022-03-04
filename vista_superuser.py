from pyexpat import model
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaSuperUser(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaSuperUsuario.ui",self)

        self.setWindowTitle("Super Usuario")

        self.lista_rol = []
        self.lista_empresa = []
        self.lista_usuarios = []

        ### USUARIO ###
        #Crear usaurio
        self.lineEdit_crear_usuario_nombre.returnPressed.connect(self.recibir_datos)
        self.lineEdit_crear_usuario_apellido.returnPressed.connect(self.recibir_datos)
        self.lineEdit_crear_usuario_password.returnPressed.connect(self.recibir_datos)

        empresa = db.session.query(Empresa).all()
        for data in empresa:
            self.lista_empresa.append(str(data))

        self.comboBox_asigna_empresa.addItems(self.lista_empresa)

        roles = db.session.query(Rol).all()
        for data in roles:
            self.lista_rol.append(str(data))

        self.comboBox_asignar_rol.addItems(self.lista_rol)
        self.pushButton_crear_usuario.clicked.connect(self.recibir_datos)

        #Editar Usuario
        self.lineEdit_editar_usuario_buscar.returnPressed.connect(self.editar_datos)
        self.pushButton_editar_usuario_buscar.clicked.connect(self.editar_datos)

        #Eliminar usuario
        self.lineEdit_eliminar_usuario_buscar.returnPressed.connect(self.buscar_datos)
        self.pushButton_eliminar_usuario_buscar.clicked.connect(self.buscar_datos)
        self.tableWidget_eliminar_usuario.setColumnCount(4)
        self.tableWidget_eliminar_usuario.setHorizontalHeaderLabels(["id","nombre","apellido","contraseña"])
        self.pushButton_eliminar_usuario.clicked.connect(self.eliminar_datos)

        #Ver usuario
        self.lineEdit_ver_usuario_buscar.returnPressed.connect(self.traer_datos)
        self.pushButton_ver_usuario_buscar.clicked.connect(self.traer_datos)
        usuarios = db.session.query(Empresa, User, Rol).select_from(Empresa).join(User).join(Rol).group_by(User.id, User.apellido, User.password, Empresa.nombre_empresa, Rol.rol_nombre).all()
        for e, u, r in usuarios:
            print("id: {}, nombre: {}, apellido: {}, contraseña: {}, empresa: {}, rol: {}".format(u.id,u.username,u.apellido,u.password,e.nombre_empresa,r.rol_nombre))

        self.tableWidget__ver_usuario.setColumnCount(6)
        self.tableWidget__ver_usuario.setHorizontalHeaderLabels(["id","nombre","apellido","contraseña","empresa","rol"])

        row = 0
        for e, u, r in usuarios:
            self.tableWidget__ver_usuario.insertRow(row)
            id = QTableWidgetItem(str(u.id))
            nombre = QTableWidgetItem(str(u.username))
            apellido = QTableWidgetItem(str(u.apellido))
            password = QTableWidgetItem(str(u.password))
            empresa = QTableWidgetItem(str(e.nombre_empresa))
            rol = QTableWidgetItem(str(r.rol_nombre))
            self.tableWidget__ver_usuario.setItem(row,0,id)
            self.tableWidget__ver_usuario.setItem(row,1,nombre)
            self.tableWidget__ver_usuario.setItem(row,2,apellido)
            self.tableWidget__ver_usuario.setItem(row,3,password)
            self.tableWidget__ver_usuario.setItem(row,4,empresa)
            self.tableWidget__ver_usuario.setItem(row,5,rol)
            row = row + 1

    def recibir_datos(self):
        nombre = self.lineEdit_crear_usuario_nombre.text()
        apellido = self.lineEdit_crear_usuario_apellido.text()
        password = self.lineEdit_crear_usuario_password.text()
        empresa_asignada = self.comboBox_asigna_empresa.currentText()
        rol_asignado = self.comboBox_asignar_rol.currentText()

        id_rol_asignado = db.session.query(Rol.id).filter_by(rol_nombre=str(rol_asignado)).first()
        id_empresa_asignada = db.session.query(Empresa.id).filter_by(nombre_empresa=str(empresa_asignada)).first()

        try:
            usuario_creado = User(str(nombre),str(apellido),str(password),id_rol_asignado[0],id_empresa_asignada[0])
            db.session.add(usuario_creado)
            db.session.commit()

            mensaje = QMessageBox()
            mensaje.setText("Usuario creado")
            mensaje.setInformativeText("Se ha creado el usuario satisfactoriamente")
            mensaje.setWindowTitle("Tarea completa")
            mensaje.exec_()
        except:
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Ha ocurrido un error al crear el usuario")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()
        
        self.lineEdit_crear_usuario_nombre.setText("")
        self.lineEdit_crear_usuario_apellido.setText("")
        self.lineEdit_crear_usuario_password.setText("")

    def editar_datos(self):
        var = self.lineEdit_editar_usuario_buscar.text()

        if(len(var) == 0):
            mensaje = QMessageBox()
            mensaje.setText("Por favor, ingrese un dato válido")
            mensaje.setInformativeText("El dato que ha ingresado es vacío")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()
        else:
            usuario_filtrado = db.session.query(User.username, User.apellido).filter_by(username=str(var)).all()

            for usuario in usuario_filtrado:
                usuario_concatenado = usuario[0] + " " + usuario[1]
                self.lista_usuarios.append(usuario_concatenado)
                print("Esta es la lista de usuarios", self.lista_usuarios)
        

        modelo = QStringListModel()
        modelo.setStringList(self.lista_usuarios)
        self.listView_edita_usuario.setModel(modelo)
        self.listView_edita_usuario.clicked.connect(self.llevar_datos)

    def llevar_datos(self):
        if(len(self.lista_usuarios) == 0):
            print(self.lista_usuarios)
        else:
            lista_nueva = self.lista_usuarios[0].split(" ")
            print("estas es la lista nueva", lista_nueva)
            self.usuario_filtrado = db.session.query(User.id, User.username, User.apellido, User.password, User.rol_id, User.empresa_id).filter_by(username=str(lista_nueva[0]), apellido=str(lista_nueva[1])).all()
            print("este es el usuario filtrado", self.usuario_filtrado)
            for datos in self.usuario_filtrado:
                self.id = datos[0]
                nombre = datos[1]
                apellido = datos[2]
                password = datos[3]
                id_rol = datos[4]
                id_empresa = datos[5]
        

        empresa = db.session.query(Empresa).get(id_empresa)
        rol = db.session.query(Rol).get(id_rol)

        self.lineEdit_editar_nombre_usuario.setText(nombre)
        self.lineEdit_editar_apellido_usuario.setText(apellido)
        self.lineEdit_editar_password_usuario.setText(password)
        self.label_rol_editar_usuario.setText(str(rol))
        self.comboBox_editar_rol_usuario.addItems(self.lista_rol)
        self.label_empresa_editar_usuario.setText(str(empresa))
        self.comboBox_editar_empresa_usuario.addItems(self.lista_empresa)
        
        self.lineEdit_editar_nombre_usuario.returnPressed.connect(self.guardar_datos)
        self.lineEdit_editar_apellido_usuario.returnPressed.connect(self.guardar_datos)
        self.lineEdit_editar_password_usuario.returnPressed.connect(self.guardar_datos)

        self.pushButton_editar_guardar_usuario.clicked.connect(self.guardar_datos)

    def guardar_datos(self):
        nuevo_nombre = self.lineEdit_editar_nombre_usuario.text()
        nuevo_apellido = self.lineEdit_editar_apellido_usuario.text()
        nueva_password = self.lineEdit_editar_password_usuario.text()
        nuevo_rol_usuario = self.comboBox_editar_rol_usuario.currentText()
        nueva_empresa_asignada = self.comboBox_editar_empresa_usuario.currentText()
        
        rol = db.session.query(Rol.id).filter(Rol.rol_nombre == nuevo_rol_usuario).first()
        empresa = db.session.query(Empresa.id).filter(Empresa.nombre_empresa == nueva_empresa_asignada).first()
        
        try:
            user_edit = db.session.query(User).filter(User.id == int(self.id)).first()
            user_edit.username = nuevo_nombre
            user_edit.apellido = nuevo_apellido
            user_edit.password = nueva_password
            user_edit.rol_id = int(rol[0])
            user_edit.empresa_id = int(empresa[0])

            db.session.add(user_edit)
            db.session.commit()

            mensaje = QMessageBox()
            mensaje.setText("El usuario ha sido creado")
            mensaje.setInformativeText("Se cumplió la tarea satisfactoriamente")
            mensaje.setWindowTitle("Tarea Completada")
            mensaje.exec_()

        except:
            mensaje = QMessageBox()
            mensaje.setText("Error al editar el usuario")
            mensaje.setInformativeText("Hubo un error al editar al usuario")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()

        lista_vacia = []

        self.lineEdit_editar_usuario_buscar.setText("")
        modelo = QStringListModel()
        modelo.setStringList(lista_vacia)
        self.listView_edita_usuario.setModel(modelo)

        self.lineEdit_editar_nombre_usuario.setText("")
        self.lineEdit_editar_apellido_usuario.setText("")
        self.lineEdit_editar_password_usuario.setText("")
        self.label_rol_editar_usuario.setText("ROL")
        self.comboBox_editar_rol_usuario.clear()
        self.label_empresa_editar_usuario.setText("EMPRESA")
        self.comboBox_editar_empresa_usuario.clear()

    def buscar_datos(self):
        palabra_escrita = self.lineEdit_eliminar_usuario_buscar.text()
        
        if(len(palabra_escrita) == 0):
            mensaje = QMessageBox()
            mensaje.setText("Por favor, ingrese un dato válido")
            mensaje.setInformativeText("El dato que ha ingresado es vacío")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()
        else:
            try:
                usuario = db.session.query(User.id, User.username, User.apellido, User.password).filter_by(username = palabra_escrita).all()
                print(usuario)
            except:
                print("Hay un error")
        
        row = 0
        for data in usuario:
            self.tableWidget_eliminar_usuario.insertRow(row)
            id = QTableWidgetItem(str(data[0]))
            nombre = QTableWidgetItem(str(data[1]))
            print(nombre)
            apellido = QTableWidgetItem(str(data[2]))
            password = QTableWidgetItem(str(data[3]))
            self.tableWidget_eliminar_usuario.setItem(row,0,id)
            self.tableWidget_eliminar_usuario.setItem(row,1,nombre)
            self.tableWidget_eliminar_usuario.setItem(row,2,apellido)
            self.tableWidget_eliminar_usuario.setItem(row,3,password)
            row = row + 1

    def eliminar_datos(self):
        rows = self.tableWidget_eliminar_usuario.selectionModel().selectedRows()
        index = []
        for i in rows:
            index.append(i.row())
        index.sort(reverse=True)
        for i in index:
            id = self.tableWidget_eliminar_usuario.item(i,0).text()
            self.tableWidget_eliminar_usuario.removeRow(i)
            db.session.query(User).filter(User.id == id).delete()
        db.session.commit()

    def traer_datos(self):
        palabra_escrita = self.lineEdit_ver_usuario_buscar.text()
        
        if(len(palabra_escrita) == 0):
            mensaje = QMessageBox()
            mensaje.setText("Por favor, ingrese un dato válido")
            mensaje.setInformativeText("El dato que ha ingresado es vacío")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()
        else:
            try:
               self.tableWidget__ver_usuario.clear()
               usuario = db.session.query(User.id, User.username, User.apellido, User.password, User.empresa_id, User.rol_id).filter_by(username = palabra_escrita).all()
               print(usuario)
               row = 0
               for data in usuario:
                   self.tableWidget__ver_usuario.insertRow(row)
                   id = QTableWidgetItem(str(data[0]))
                   nombre = QTableWidgetItem(str(data[1]))
                   apellido = QTableWidgetItem(str(data[2]))
                   password = QTableWidgetItem(str(data[3]))
                   empresa = QTableWidgetItem(str(db.session.query(Empresa).get(data[4])))
                   rol = QTableWidgetItem(str(db.session.query(Rol).get(data[5])))
                   self.tableWidget__ver_usuario.setItem(row,0,id)
                   self.tableWidget__ver_usuario.setItem(row,1,nombre)
                   self.tableWidget__ver_usuario.setItem(row,2,apellido)
                   self.tableWidget__ver_usuario.setItem(row,3,password)
                   self.tableWidget__ver_usuario.setItem(row,4,empresa)
                   self.tableWidget__ver_usuario.setItem(row,5,rol)
                   row = row + 1                
            except:
                print("Hay un error")

def main():
    app = QApplication(sys.argv)
    window = VistaSuperUser()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    