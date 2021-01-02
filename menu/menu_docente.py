from arreglo.arreglo_docente import array_docente
from clases.docente import Docente
from otro.validacion import Validacion

class MenuDocente:
    def menu(self):
        while True:
            print('''
                Menú Docente
                1) Agregar Docente
                2) Eliminar Docente
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
        
        dd=array_docente()
        codigo=dd.codigo_correlativo()
        while True:
            codigo_curso=input(f"ingrese codigo de Curso:\n")
            if Validacion.validar_codigo_curso(codigo_curso):
                break   
            else:
                print(f"Error-ingrese un codigo de curso valido\n")
        nombre=Validacion.validar_texto('Ingrese el nombre del Docente')
        apellido=Validacion.validar_texto('Ingrese el Apellido del Docente')
        dni=Validacion.validar_dni('Ingresar el DNI del Docente')
        edad=Validacion.validar_edad('Ingresar la edad del Docente')
        dd.agregar(Docente(codigo,codigo_curso,nombre,apellido,dni,edad))
        self.menu()

    def eliminar(self):
        Validacion.validar_codigo('docente')
        self.menu()