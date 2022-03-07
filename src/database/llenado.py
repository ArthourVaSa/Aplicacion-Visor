import os

from modelos import *

from db import *

def main():
    
    #creo los modulos a usar
    modulo1 = Modulo('Usuario')
    modulo2 = Modulo('Empresa')
    modulo3 = Modulo('Rol')
    modulo4 = Modulo('Area')
    modulo5 = Modulo('Tipo Documental')
    modulo6 = Modulo('Indice de Búsqueda')

    #subo los datos a la bd
    db.session.add(modulo1)
    db.session.add(modulo2)
    db.session.add(modulo3)
    db.session.add(modulo4)
    db.session.add(modulo5)
    db.session.add(modulo6)
    
    #creo los roles de usuario
    rol1 = Rol('SuperUsuario')
    rol2 = Rol('Administrador')
    rol3 = Rol('Usuario')

    #subo los datos a la bd
    db.session.add(rol1)
    db.session.add(rol2)
    db.session.add(rol3)

    #confirmo los cambios en la bd
    db.session.commit()

    #creo las operaciones por modulo
    operacion1 = Operaciones('crear_usuario',modulo1.id)
    operacion2 = Operaciones('editar_usuario',modulo1.id)
    operacion3 = Operaciones('eliminar_usuario',modulo1.id)
    operacion4 = Operaciones('ver_usuario',modulo1.id)
    operacion5 = Operaciones('crear_empresa',modulo2.id)
    operacion6 = Operaciones('editar_empresa',modulo2.id)
    operacion7 = Operaciones('eliminar_empresa',modulo2.id)
    operacion8 = Operaciones('ver_empresa',modulo2.id)
    operacion9 = Operaciones('asignar_empresa',modulo2.id)
    operacion10 = Operaciones('desasignar_empresa',modulo2.id)
    operacion11 = Operaciones('asignar_rol',modulo3.id)
    operacion12 = Operaciones('desasignar_rol', modulo3.id)
    operacion13 = Operaciones('crear_area',modulo4.id)
    operacion14 = Operaciones('editar_area',modulo4.id)
    operacion15 = Operaciones('eliminar_area',modulo4.id)
    operacion16 = Operaciones('ver_area',modulo4.id)
    operacion17 = Operaciones('asignar_area',modulo4.id)
    operacion18 = Operaciones('desasignar_area',modulo4.id)
    operacion19 = Operaciones('crear_tipo_doc',modulo5.id)
    operacion20 = Operaciones('editar_tipo_doc',modulo5.id)
    operacion21 = Operaciones('eliminar_tipo_doc',modulo5.id)
    operacion22 = Operaciones('ver_tipo_doc',modulo5.id)
    operacion23 = Operaciones('asignar_tipo_doc',modulo5.id)
    operacion24 = Operaciones('desasignar_tipo_doc',modulo5.id)

    #subo los datos a la bd
    db.session.add(operacion1)
    db.session.add(operacion2)
    db.session.add(operacion3)
    db.session.add(operacion4)
    db.session.add(operacion5)
    db.session.add(operacion6)
    db.session.add(operacion7)
    db.session.add(operacion8)
    db.session.add(operacion9)
    db.session.add(operacion10)
    db.session.add(operacion11)
    db.session.add(operacion12)
    db.session.add(operacion13)
    db.session.add(operacion14)
    db.session.add(operacion15)
    db.session.add(operacion16)
    db.session.add(operacion17)
    db.session.add(operacion18)
    db.session.add(operacion19)
    db.session.add(operacion20)
    db.session.add(operacion21)
    db.session.add(operacion22)
    db.session.add(operacion23)
    db.session.add(operacion24)

    #confirmo los cambios en la bd
    db.session.commit()

    #creo las relaciones de rol-operacion
    rol1.operaciones_rol += [operacion1,operacion2,operacion3,operacion4,operacion5,operacion6,operacion7,operacion8,operacion9,operacion10,operacion11,operacion12]
    rol2.operaciones_rol += [operacion13,operacion14,operacion15,operacion16,operacion17,operacion18,operacion19,operacion20,operacion21,operacion22,operacion23,operacion24]
    rol3.operaciones_rol += [operacion8,operacion16,operacion22]

    #Confirmo los datos subidos a la bd
    db.session.commit()

    #Creo una empresa
    empresa1 = Empresa('Nexuss Enterprise')

    #Subo los datos a la bd
    db.session.add(empresa1)

    #Confirmo los datos subidos a la bd
    db.session.commit()

    #Creo un usuario con su empresa
    usuario1 = User('Arthour','Vásquez','123456',rol1.id,empresa1.id)

    #Subo los datos a la bd
    db.session.add(usuario1)

    #Confirmo los datos
    db.session.commit()

    #creo el area
    area1 = Area('Logística-Nexuss',empresa1.id)
    area2 = Area('Contabilidad-Nexuss',empresa1.id)

    #subo los datos a la bd
    db.session.add(area1) 
    db.session.add(area2)

    #confirmo datos subidos
    db.session.commit()

    archivo = os.path.basename("D:/Arthour/Trabajos/Nexuzz/Archivos/archivos/src/database/CV.pdf")
    tipodocumental1 = TipoDoc('factura',archivo,1)

    db.session.add(tipodocumental1)
    db.session.commit()

if __name__ == '__main__':
    db.Base.metadata.drop_all(db.engines)
    db.Base.metadata.create_all(db.engines)
    main()