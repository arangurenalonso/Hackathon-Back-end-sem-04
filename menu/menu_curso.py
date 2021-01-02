from arreglo.arreglo_curso import array_curso
from clases.curso import Curso
from otro.validacion import Validacion

class MenuCurso:
    def menu(self):
        while True:
            print('''
                Menú Curso
                1) Agregar Curso
                2) Eliminar Curso
                3) Ir al MENU PRINCIPAL
            \n''')
            opcion = input('Ingresa el n° : ')
            if opcion == '1':
                self.agregar()
                break
            elif opcion == '2':
                self.eliminar()
                break
            elif opcion == '3':
                break
            else:
                print('No escogiste una opción valida')

    def agregar(self):
        
        cc=array_curso()
        codigo=cc.codigo_correlativo()
        nombre_curso=Validacion.validar_texto('Ingrese el nombre del Curso')
        cc.agregar(Curso(codigo,nombre_curso))
        self.menu()
    
    def eliminar(self):
        Validacion.validar_codigo('curso')
        self.menu()


