from sqlalchemy import Column, String, Integer, Boolean
import db

class Tarea(db.Base):

    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    fecha = Column(String(12))  # Con 10 valdria (DD/MM/AAAA) pero por si acaso para que no de error
    categoria = Column(String(100))

    def __init__(self, contenido, hecha, fecha, categoria):
        self.contenido = contenido
        self.hecha = hecha
        self.fecha = fecha
        self.categoria = categoria

    def __str__(self):
        return "({}: {} {})".format(self.id, self.contenido, self.hecha)