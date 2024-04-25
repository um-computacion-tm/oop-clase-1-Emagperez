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
    def __init__(self,nombre, legajo, edad, email, inasistencias):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__edad__ = edad
        self.__email__ = email
        self.__inasistencias__ = 0
        self.__mentor__ = None
    
    def agregar_mentor(self,mentor):
        self.__mentor__ = mentor

    def cambiar_emai(self, email):
        self.__email__ = email

    def cambiar_edad(self,edad):
        self.__edad__ = edad

alumno_camila = Alumno(nombre = "Camila", legajo = 123, edad = 21, email = "camila@gmail.com",inasistencias=0)
print("instancia de la clase: ",alumno_camila)
print("clase alumno", Alumno)
print("Mentor de camila: ",alumno_camila.__nombre__," es ",alumno_camila.__mentor__)
alumno_camila.agregar_mentor("Carlos")
print("Mentor de camila: ",alumno_camila.__nombre__," es ",alumno_camila.__mentor__)
alumno_ema = Alumno(nombre = "Ema", legajo= 234, edad=21,email="ema@gmail.com",inasistencias=1)
alumno_ema.cambiar_edad(23)
print(alumno_ema.__edad__)

Daniel = Profesor( "daniel","titular",123)
WAlter = Profesor( "Walter","ayudante",321)

print(Daniel.__legajo__)

materia_comp = Materias(
    "Computacion",profesores = [Daniel,WAlter])
profesores_de_comp = materia_comp.obtener_profesores
print("profesores de comp ", profesores_de_comp)