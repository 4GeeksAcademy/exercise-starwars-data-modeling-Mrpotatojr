import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    
    favoritos: Mapped["Favoritos"] = relationship()

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    usuario: Mapped["Usuario"] = relationship()

    planeta_id: Mapped[int] = mapped_column(ForeignKey('planetas.id'))
    planeta: Mapped["Planetas"] = relationship()
    
    personaje_id: Mapped[int] = mapped_column(ForeignKey('person.id'))
    persona: Mapped["Person"] = relationship()

class Planetas(Base):
    __tablename__ = 'planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gravity: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    diameter: Mapped[int] = mapped_column(nullable=False)
    
    favoritos: Mapped["Favoritos"] = relationship()

class Person(Base):
    __tablename__ = 'person'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    birthyear: Mapped[str] = mapped_column(nullable=False)
    eyecolor: Mapped[str] = mapped_column(nullable=False)

    favoritos: Mapped["Favoritos"] = relationship()

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
