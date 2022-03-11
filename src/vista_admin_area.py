from pyexpat import model
import sys
from tkinter import E

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from database import db
from database.modelos import *

class VistaAdminArea(QDialog):

    def __init__(self, texto):
        QDialog.__init__(self)
        uic.loadUi("vistas/VistaAdminArea.ui",self)

        self.texto = texto

        self.setWindowTitle("Administrador")

        self.label_empresa.setText(self.texto)

        #agregar area
        self.lineEdit_nombre_area.returnPressed.connect(self.agregar_area)
        self.pushButton_agregar_area.clicked.connect(self.agregar_area)

        #parte de la tabla
        self.tableWidget_area.setColumnCount(2)
        self.tableWidget_area.setHorizontalHeaderLabels(["id","Área"])
        
        empresa_id = db.session.query(Empresa.id).filter(Empresa.nombre_empresa == self.texto).first()
        areas = db.session.query(Area.id, Area.nombre_area).filter(empresa_id[0] == Area.id_empresa).all()
        row = 0
        for area in areas:
            self.tableWidget_area.insertRow(row)
            id = QTableWidgetItem(str(area.id))
            nombre = QTableWidgetItem(str(area.nombre_area))
            self.tableWidget_area.setItem(row,0,id)
            self.tableWidget_area.setItem(row,1,nombre)
            row = row + 1

        #parte editar
        self.pushButton_editar_area.clicked.connect(self.editar_area)

        #parte eliminar
        self.pushButton_eliminar_area.clicked.connect(self.eliminar_area)

    def agregar_area(self):
        nombre_area = self.lineEdit_nombre_area.text()

        if (len(nombre_area) == 0):
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Por favor inserte el nombre del área a crear")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()
        else:
            try:
                self.id_empresa = db.session.query(Empresa.id).filter(Empresa.nombre_empresa==self.texto).first()
                self.nueva_area = Area(str(nombre_area),self.id_empresa[0])
                db.session.add(self.nueva_area)
                db.session.commit()

                mensaje = QMessageBox()
                mensaje.setText("Área agregada")
                mensaje.setInformativeText("La tarea ha sido cumplida. Se ha agregado el área satisfactoriamente")
                mensaje.setWindowTitle("Tarea completa")
                mensaje.exec_()

                self.lineEdit_nombre_area.setText("")
            except:
                mensaje = QMessageBox()
                mensaje.setText("Ha ocurrido un error.")
                mensaje.setInformativeText("Ha ocurrido un error al crear el área para la empresa")
                mensaje.setWindowTitle("ERROR")
                mensaje.exec_()

    def editar_area(self):
        try:
            row = self.tableWidget_area.currentRow()
            id = self.tableWidget_area.item(row, 0).text()
            value = self.tableWidget_area.currentItem().text()
            area_edit = db.session.query(Area).filter(Area.id == int(id)).first()
            area_edit.nombre_area = value
            db.session.add(area_edit)
            db.session.commit()

            mensaje = QMessageBox()
            mensaje.setText("Área editada")
            mensaje.setInformativeText("La tarea ha sido cumplida. Se ha editado el área satisfactoriamente")
            mensaje.setWindowTitle("Tarea completa")
            mensaje.exec_()
        except:
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Ha ocurrido un error al editar el área para la empresa")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()               
    
    def eliminar_area(self):
        try:
            rows = self.tableWidget_area.selectionModel().selectedRows()
            index = []
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id = self.tableWidget_area.item(i,0).text()
                self.tableWidget_area.removeRow(i)
                db.session.query(Area).filter(Area.id == id).delete()
            db.session.commit()

            mensaje = QMessageBox()
            mensaje.setText("Área Eliminada")
            mensaje.setInformativeText("La tarea ha sido cumplida. Se ha eliminado el área satisfactoriamente")
            mensaje.setWindowTitle("Tarea completa")
            mensaje.exec_()
        except:
            mensaje = QMessageBox()
            mensaje.setText("Ha ocurrido un error.")
            mensaje.setInformativeText("Ha ocurrido un error al eliminar el área para la empresa")
            mensaje.setWindowTitle("ERROR")
            mensaje.exec_()   

# def main():
#     app = QApplication(sys.argv)
#     window = VistaAdminArea()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()