from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import DateTime, Integer, String

engines = create_engine('sqlite:///D:/Arthour/Trabajos/Nexuzz/Archivos/archivos/database/archivosdb.db')

Session = sessionmaker(engines)
session = Session()

Base = declarative_base()