import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.config import Base

class Autores(Base):
    __tablename__ = "autores"

    id_autor = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    nacionalidad = Column(String(50), unique=True, index=True, nullable=False)
    bibliografia = Column(String(200), unique=True, index=True, nullable=False)
    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())


    def __repr__(self):
        return f"<nombre='{self.nombre}', nacionalidad='{self.nacionalidad}' bibliografia='{self.bibliografia}')>"
