import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.config import Base

class Items(Base):
    """Modelo de Producto"""

    __tablename__ = "items"

    id_items = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_autor = Column(UUID(as_uuid=True), ForeignKey("autores.id_autor"), nullable=False)
    titulo = Column(String(255), nullable=False)
    disponible = Column(Boolean, default=True)
    tipo_item = Column(String(20), nullable=False)
    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())


    def __repr__(self):
        return f"<Items(id_items={self.id_producto}, id_autor='{self.id_autor}', titulo='{self.titulo}')>"
