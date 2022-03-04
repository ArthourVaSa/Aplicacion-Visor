from pyexpat import model
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaSuperEmpresa(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaSuperEmpresa.ui",self)

        self.setWindowTitle("Super Usuario")

        #crear empresa
        self.lineEdit_crear_empresa.returnPressed.connect(self.crear_empresa)
        self.pushButton_crear_empresa.clicked.connect(self.crear_empresa)

        #editar empresa
        self.tableWidget_editar_empresa.setColumnCount(2)
        self.tableWidget_editar_empresa.setHorizontalHeaderLabels(["id","nombre"])

        empresas = db.session.query(Empresa).all()
        row = 0
        for empresa in empresas:
            self.tableWidget_editar_empresa.insertRow(row)
            id = QTableWidgetItem(str(empresa.id))
            nombre = QTableWidgetItem(str(empresa.nombre_empresa))
            self.tableWidget_editar_empresa.setItem(row,0,id)
            self.tableWidget_editar_empresa.setItem(row,1,nombre)
            row = row + 1

        self.tableWidget_editar_empresa.itemChanged.connect(self.editar_empresa)
        self.pushButton_editar_empresa.clicked.connect(self.editar_empresa)

        #eliminar empresa
        self.tableWidget_eliminar_empresa.setColumnCount(2)
        self.tableWidget_eliminar_empresa.setHorizontalHeaderLabels(["id","nombre"])

        empresas = db.session.query(Empresa).all()
        row = 0
        for empresa in empresas:
            self.tableWidget_eliminar_empresa.insertRow(row)
            id = QTableWidgetItem(str(empresa.id))
            nombre = QTableWidgetItem(str(empresa.nombre_empresa))
            self.tableWidget_eliminar_empresa.setItem(row,0,id)
            self.tableWidget_eliminar_empresa.setItem(row,1,nombre)
            row = row + 1

        self.pushButton_eliminar_empresa.clicked.connect(self.eliminar_empresa)

        #ver empresa
        self.tableWidget_ver_empresa.setColumnCount(2)
        self.tableWidget_ver_empresa.setHorizontalHeaderLabels(["id","nombre"])

        empresas = db.session.query(Empresa).all()
        row = 0
        for empresa in empresas:
            self.tableWidget_ver_empresa.insertRow(row)
            id = QTableWidgetItem(str(empresa.id))
            nombre = QTableWidgetItem(str(empresa.nombre_empresa))
            self.tableWidget_ver_empresa.setItem(row,0,id)
            self.tableWidget_ver_empresa.setItem(row,1,nombre)
            row = row + 1

    def crear_empresa(self):
        nombre_empresa = self.lineEdit_crear_empresa.text()
        if(len(nombre_empresa)==0):
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Por favor inserte el nombre de la empresa a crear")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()
        else:
            try:
                empresa_creada = Empresa(str(nombre_empresa))
                print(empresa_creada)
                db.session.add(empresa_creada)
                db.session.commit()

                mensaje = QMessageBox()
                mensaje.setText("Empresas creada")
                mensaje.setInformativeText("La tarea ha sido cumplida. Se ha creado la empresa satisfactoriamente")
                mensaje.setWindowTitle("Tarea completa")
                mensaje.exec_()

                self.lineEdit_crear_empresa.setText("")
            except:
                mensaje = QMessageBox()
                mensaje.setText("Ha ocurrido un error.")
                mensaje.setInformativeText("Ha ocurrido un error al crear la empresa")
                mensaje.setWindowTitle("ERROR")
                mensaje.exec_()

    def editar_empresa(self):
        try:
            column = self.tableWidget_editar_empresa.currentColumn()
            row = self.tableWidget_editar_empresa.currentRow()
            id = self.tableWidget_editar_empresa.item(row, 0).text()
            value = self.tableWidget_editar_empresa.currentItem().text()
            columns = ["id","nombre"]
            empresa_edit = db.session.query(Empresa).filter(Empresa.id == int(id)).first()
            print(empresa_edit)
            empresa_edit.nombre_empresa = value

            db.session.add(empresa_edit)
            db.session.commit()          
        except:
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Ha ocurrido un error al editar la empresa")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()

    def eliminar_empresa(self):
        try:
            rows = self.tableWidget_eliminar_empresa.selectionModel().selectedRows()
            index = []
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id = self.tableWidget_eliminar_empresa.item(i,0).text()
                self.tableWidget_eliminar_empresa.removeRow(i)
                db.session.query(Empresa).filter(Empresa.id == id).delete()
            db.session.commit()
        except:
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Ha ocurrido un error al eliminar la empresa")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()

    def ver_empresa(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = VistaSuperEmpresa()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()