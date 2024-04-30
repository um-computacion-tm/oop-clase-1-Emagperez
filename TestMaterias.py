import unittest
from Alumno import Alumno, Profesor, Materias

class TestMaterias(unittest.TestCase):
    def setUp(self):
        self.profesor1 = Profesor("Jennifer Aniston", "Profesor de Matemáticas", "801")
        self.profesor2 = Profesor("Courteney Cox", "Profesora de Historia", "802")
        self.alumno1 = Alumno("Rachel Green", "701", 24, "rachel@gmail.com", 0)
        self.alumno2 = Alumno("Monica Geller", "702", 26, "monica@gmail.com", 0)
        self.alumno3 = Alumno("Phoebe Buffay", "703", 28, "phoebe@gmail.com", 0)
        self.alumno4 = Alumno("Joey Tribbiani", "704", 25, "joey@gmail.com", 0)
        self.alumno5 = Alumno("Chandler Bing", "705", 27, "chandler@gmail.com", 0)
        self.alumno6 = Alumno("Ross Geller", "706", 29, "ross@gmail.com", 0)
        self.materia = Materias("Matemáticas", [self.profesor1, self.profesor2], [self.alumno1, self.alumno2, self.alumno3, self.alumno4, self.alumno5, self.alumno6])

    def test_obtener_profesores(self):
        profesores = self.materia.obtener_profesores()
        self.assertEqual(len(profesores), 2)
        self.assertIn(self.profesor1, profesores)
        self.assertIn(self.profesor2, profesores)

    def test_obtener_alumnos(self):
        alumnos = self.materia.obtener_alumnos()
        self.assertEqual(len(alumnos), 6)
        self.assertIn(self.alumno1, alumnos)
        self.assertIn(self.alumno2, alumnos)
        self.assertIn(self.alumno3, alumnos)
        self.assertIn(self.alumno4, alumnos)
        self.assertIn(self.alumno5, alumnos)
        self.assertIn(self.alumno6, alumnos)

class TestProfesor(unittest.TestCase):
    def setUp(self):
        self.profesor = Profesor("Jennifer Aniston", "Profesor de Matemáticas", "801")

    def test_obtener_nombre(self):
        self.assertEqual(self.profesor.obtener_nombre(), "Jennifer Aniston")

    def test_obtener_cargo(self):
        self.assertEqual(self.profesor.obtener_cargo(), "Profesor de Matemáticas")

    def test_obtener_legajo(self):
        self.assertEqual(self.profesor.obtener_legajo(), "801")

class TestAlumno(unittest.TestCase):
    def setUp(self):
        self.alumno = Alumno("Rachel Green", "701", 24, "rachel@gmail.com", 0)

    def test_agregar_mentor(self):
        mentor = Profesor("Courteney Cox", "Profesor de Matemáticas", "802")
        self.alumno.agregar_mentor(mentor)
        self.assertEqual(self.alumno.obtener_mentor(), mentor)

    def test_cambiar_email(self):
        nuevo_email = "rachel.green@example.com"
        self.alumno.cambiar_email(nuevo_email)
        self.assertEqual(self.alumno.obtener_email(), nuevo_email)

    def test_cambiar_edad(self):
        nueva_edad = 25
        self.alumno.cambiar_edad(nueva_edad)
        self.assertEqual(self.alumno.obtener_edad(), nueva_edad)

if __name__ == '__main__':
    unittest.main()