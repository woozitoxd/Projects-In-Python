from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


#Creamos la clase Empleado que hereda de database.Model
#Esta clase representa la tabla empleados en la base de datos.

class Empleado(database.Model):
    __tablename__ = 'empleados'  
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    puesto = database.Column(database.String(100))
    salario = database.Column(database.Float)


