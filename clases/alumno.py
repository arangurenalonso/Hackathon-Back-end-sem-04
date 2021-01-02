from clases.persona import Persona

class Alumno(Persona):
    def __init__(self,cod_alumno,nombre,apellido,dni,edad):
        self.cod_alumno=cod_alumno
        super().__init__(nombre,apellido,dni,edad)
        


