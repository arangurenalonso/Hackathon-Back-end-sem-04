from arreglo.arreglo_alumno import array_alumno
from clases.alumno import Alumno
from otro.validacion import Validacion

class MenuAlumno:
    def menu(self):
        while True:
            print('''
                Menú Alumno
                1) Agregar Alumno
                2) Eliminar Alumno
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
        
        aa=array_alumno()
        codigo=aa.codigo_correlativo()
        nombre=Validacion.validar_texto('Ingrese el nombre del Alumno')
        apellido=Validacion.validar_texto('Ingrese el Apellido del Alumno')
        dni=Validacion.validar_dni('Ingresar el DNI del Alumno')
        edad=Validacion.validar_edad('Ingresar la edad del Alumno')
        aa.agregar(Alumno(codigo,nombre,apellido,dni,edad))
        self.menu()

    def eliminar(self):
        Validacion.validar_codigo('alumno')
        self.menu()
