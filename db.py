from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Usamos el engine para crear y conectarnos a una base de datos
engine = create_engine("sqlite:///database/tarea.db", connect_args={"check_same_thread": False})

# Siguiente, necesitamos una sesion para mandarle ordenes (transacciones) a la bbdd hay que crearla y ya usarla
Session = sessionmaker(bind=engine)
session = Session()
# Es la variable con la que haremos cosas en la bbdd, y con esta ultima linea hemos activado la Session

# Es el que mapea y traduce las clases a tablas, creando las estructuras
Base = declarative_base()
