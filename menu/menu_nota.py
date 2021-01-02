from arreglo.arreglo_nota import array_nota
from clases.nota import Nota
from otro.validacion import Validacion


class MenuNota:
    def menu(self):
        while True:
            print('''
                Menú Nota
                1) Agregar Nota
                2) Eliminar Nota
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
        
        nn=array_nota()
        codigo=nn.codigo_correlativo()
        while True:
            codigo_alumno=input(f"ingrese codigo del Alumno:\n")
            if Validacion.validar_codigo_alumno(codigo_alumno):
                break   
            else:
                print(f"Error-ingrese un codigo de Alumno valido\n")
        
        while True:
            codigo_curso=input(f"ingrese codigo de Curso:\n")
            if Validacion.validar_codigo_curso(codigo_curso):
                break   
            else:
                print(f"Error-ingrese un codigo de curso valido\n")
        lista_notas=self.ingresar_notas()
        maximo=max(lista_notas)
        minimo=min(lista_notas)
        promedio=sum(lista_notas)/len(lista_notas)


        nn.agregar(Nota(codigo,codigo_alumno,codigo_curso,lista_notas,maximo,minimo,promedio))
        self.menu()

    def eliminar(self):
        Validacion.validar_codigo('nota')
        self.menu()

    def ingresar_notas(self):
        while True:
            try:
                while True:
                    cantNotasIngresar=int(input(f"Ingrese la cantidad de notas a ingresar:\n"))
                    if cantNotasIngresar>=0:
                        break
                    else:
                        print("Ingrese un numero mayor a 0")
                break

            except ValueError:
                print(f'Ingrese un numero')

        notas=[]

        for i in range(0,cantNotasIngresar,1):
            while True:
                try:
                    while True:
                        nota=float(input(f"Ingrese la nota {i+1}:\n"))
                        if nota>=0 and nota<=20:
                            notas.append(nota)
                            break
                        else:
                            print("Ingrese una nota entre 0 a 20")
                    break

                except ValueError:
                    print(f'Ingrese un numero valido')
        return notas