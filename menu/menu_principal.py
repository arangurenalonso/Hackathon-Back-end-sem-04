from arreglo.arreglo_alumno import array_alumno
from clases.alumno import Alumno
from menu.menu_alumno import MenuAlumno

from arreglo.arreglo_docente import array_docente
from clases.docente import Docente
from menu.menu_docente import MenuDocente

from arreglo.arreglo_curso import array_curso
from clases.curso import Curso
from menu.menu_curso import MenuCurso

from arreglo.arreglo_nota import array_nota
from clases.nota import Nota
from menu.menu_nota import MenuNota

class Inicio:
    def __init__(self):
        pass

    def menu(self):
        while True:
            print('''
                Menú:

                1) Ir a -> ALUMNO
                2) Ir a -> CURSO 
                3) Ir a -> DOCENTE
                4) Ir a -> NOTAS
                5) SALIR
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                alumno = MenuAlumno()
                alumno.menu()
            elif opcion == '2':
                curso = MenuCurso()
                curso.menu()
            elif opcion == '3':
                docente = MenuDocente()
                docente.menu()
            elif opcion == '4':
                nota = MenuNota()
                nota.menu()
            elif opcion == '5':
                break
            else:
                print('No escogiste una opción valida')
    


