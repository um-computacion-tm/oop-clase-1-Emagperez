class Materias:
    def __init__(self,nombre, profesores,alumnos):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def obtener_alumnos(self):
        return self.__alumnos__
       

class Profesor:
    def __init__(self,nombre,cargo,legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo
    
    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_cargo(self):
        return self.__cargo__
    
    def obtener_legajo(self):
        return self.__legajo__
    


class Alumno:
    def __init__(self, nombre, legajo, edad, email, inasistencias):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__edad__ = edad
        self.__email__ = email
        self.__inasistencias__ = 0
        self.__mentor__ = None
    
    def agregar_mentor(self, mentor):
        self.__mentor__ = mentor

    def obtener_mentor(self):
        return self.__mentor__

    def cambiar_email(self, email):
        self.__email__ = email

    def obtener_email(self):
        return self.__email__

    def cambiar_edad(self, edad):
        self.__edad__ = edad

    def obtener_edad(self):
        return self.__edad__


