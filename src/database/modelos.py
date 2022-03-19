from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime

from database import db
# import db

usuario_tip_doc = Table(
    'usuario_tipo_documental', db.Base.metadata,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('id_usuario', Integer, ForeignKey('users.id')),
    Column('id_tipo_doc', Integer, ForeignKey('tipodocumental.id'))
)

user_area = Table(
    'usuario_area', db.Base.metadata,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('id_usuario', Integer, ForeignKey('users.id')),
    Column('id_area', Integer, ForeignKey('area.id')),
    Column('id_empresa', Integer,nullable=false)
)

class User(db.Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    rol_id = Column(Integer(), ForeignKey('rol.id'))
    empresa_id = Column(Integer(), ForeignKey('empresa.id'))
    tipo_documental = relationship('TipoDoc',
                      secondary=usuario_tip_doc,
                      back_populates='usuarios'
    )
    area = relationship(
        'Area',
        secondary=user_area,
        back_populates='usuarios'
    )

    def __init__(self, nombre, apellido, contraseña,rol_id,empresa_id):
        self.username = nombre
        self.apellido = apellido
        self.password = contraseña
        self.rol_id = rol_id
        self.empresa_id = empresa_id

    def __repr__(self):
        return f'User((self.username),(self.apellido),(self.password),(self.empresa_id),(self.rol_id),(self.empresa_id))'

    def __str__(self):
        return self.username

rol_operaciones = Table(
    'rol_operaciones', db.Base.metadata,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('id_rol', Integer, ForeignKey('rol.id')),
    Column('id_operacion', Integer, ForeignKey('operaciones.id'))
)

class Rol(db.Base):
    __tablename__ = 'rol'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    rol_nombre = Column(String(50),nullable=False, unique=True)
    operaciones_rol = relationship('Operaciones',
                      secondary=rol_operaciones,
                      back_populates='roles'
    )
    usuario = relationship('User',backref='rol')

    def __init__(self, nombre):
        self.rol_nombre = nombre

    def __repr__(self):
        return f'Rol((self.nombre))'

    def __str__(self):
        return self.rol_nombre       

class Operaciones(db.Base):
    __tablename__ = 'operaciones'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    operacion_nombre = Column(String(50),nullable=False, unique=True)
    roles = relationship(
        'Rol', 
        secondary=rol_operaciones,
        back_populates='operaciones_rol'
    )
    modelo_id = Column(Integer, ForeignKey('modulo.id'))

    def __init__(self, nombre_operacion, modulo):
        self.operacion_nombre = nombre_operacion
        self.modelo_id = modulo

    def __repr__(self):
        return f'Operaciones(self.operacion_nombre, self.modelo_id)'

    def __str__(self):
        return self.operacion_nombre

class Modulo(db.Base):
    __tablename__ = 'modulo'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    modulo_nombre = Column(String(50), nullable=False, unique=True)
    operacion = relationship('Operaciones', backref='modulo')

    def __init__(self, nombre_modulo):
        self.modulo_nombre = nombre_modulo

    def __repr__(self):
        return f'Modulo(self.modulo_nombre)'

    def __str__(self):
        return self.modulo_nombre
    
class Empresa(db.Base):
    __tablename__ = 'empresa'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    nombre_empresa = Column(String(50), nullable=False, unique=True)
    area = relationship('Area',backref='empresa')
    usuario = relationship('User',backref='empresa')

    def __init__(self, empresa_nombre):
        self.nombre_empresa = empresa_nombre

    def __repr__(self):
        return f'Empresa((self.nombre_empresa))'

    def __str__(self):
        return self.nombre_empresa

area_tipodoc = Table(
    'area_tipodoc', db.Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_area', Integer, ForeignKey('area.id')),
    Column('id_tipodoc',Integer, ForeignKey('tipodocumental.id'))
)

class Area(db.Base):
    __tablename__ = 'area'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    nombre_area = Column(String(50), nullable=False)
    tipo_doc = relationship('TipoDoc',
                      secondary=area_tipodoc,
                      back_populates='area'
    )
    id_empresa = Column(Integer(), ForeignKey('empresa.id'))
    usuarios = relationship(
        'User',
        secondary=user_area,
        back_populates='area'
    )

    def __init__(self, nombre_area, id_empresa):
        self.nombre_area = nombre_area
        self.id_empresa = id_empresa
    
    def __repr__(self):
        return f'Area((self.nombre_area),(self.id_empresa))'

    def __str__(self):
        return self.nombre_area

class TipoDoc(db.Base):
    __tablename__ = 'tipodocumental'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    tipo_doc = Column(String(50), nullable=False)
    area = relationship('Area',
                      secondary=area_tipodoc,
                      back_populates='tipo_doc'
    )
    indice_busqueda = relationship('IndiceBusqueda',backref='tipodocumental')
    usuarios = relationship('User',
                      secondary=usuario_tip_doc,
                      back_populates='tipo_documental'
    )

    def __init__(self, tipo_doc):
        self.tipo_doc = tipo_doc

    def __repr__(self):
        return f'TipoDoc((self.tipo_doc),(self.archivo))'

    def __str__(self):
        return self.tipo_doc

class IndiceBusqueda(db.Base):
    __tablename__ = 'indicebusqueda'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    nombre_archivo = Column(String(50), nullable=False)
    indice_busqueda = Column(String(10000), nullable=False)
    id_tipo_doc = Column(Integer(), ForeignKey('tipodocumental.id'))

    def __init__(self, nombre_archivo, indice_busqueda, id_tipo_doc):
        self.nombre_archivo = nombre_archivo
        self.indice_busqueda = indice_busqueda
        self.id_tipo_doc = id_tipo_doc

    def __repr__(self):
        return f'IndiceBusqueda((self.nombre_archivo),(self.indice_busqueda),(self.id_tipo_doc))'

    def __str__(self):
        return self.nombre_archivo
