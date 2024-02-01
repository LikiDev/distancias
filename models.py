from sqlalchemy import Boolean, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Tecnico(Base):
    __tablename__ = 'tecnicos'
    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String)
    estado_id = Column(Integer, ForeignKey('estados_tecnicos.id'))
    latitud = Column(Float)
    longitud = Column(Float)
    estado = relationship("EstadoTecnico", back_populates="tecnicos")
    servicios = relationship("TipoServicio", secondary="tecnicos_tipos_servicios")

class TipoServicio(Base):
    __tablename__ = 'tipos_servicios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tecnicos = relationship("Tecnico", secondary="tecnicos_tipos_servicios")

class EstadoTecnico(Base):
    __tablename__ = 'estados_tecnicos'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    tecnicos = relationship("Tecnico", back_populates="estado")

class Establecimiento(Base):
    __tablename__ = 'establecimientos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    latitud = Column(Float)
    longitud = Column(Float)

class TecnicoTipoServicio(Base):
    __tablename__ = 'tecnicos_tipos_servicios'
    id = Column(Integer, primary_key=True)
    tecnico_id = Column(Integer, ForeignKey('tecnicos.id'))
    tipo_servicio_id = Column(Integer, ForeignKey('tipos_servicios.id'))
    
class Distancia(Base):
    __tablename__ = 'distancias'
    id = Column(Integer, primary_key=True)
    id_origen = Column(Integer)  
    id_destino = Column(Integer)  
    distancia = Column(Float)
    tipo_destino = Column(Boolean)  # False para establecimiento, True para técnico