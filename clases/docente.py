from clases.persona import Persona

class Docente(Persona):
    def __init__(self,cod_docente,cod_curso,nombre, apellido,dni,edad):
        self.cod_docente=cod_docente
        self.cod_curso=cod_curso
        super().__init__(nombre, apellido,dni,edad)
        


