from arreglo.arreglo_curso import array_curso
from clases.curso import Curso

from arreglo.arreglo_alumno import array_alumno
from clases.alumno import Alumno

from arreglo.arreglo_docente import array_docente
from clases.docente import Docente

from arreglo.arreglo_nota import array_nota
from clases.nota import Nota

class Validacion:
    @classmethod
    def validar_texto(cls,Comentario):
        texto=""
        while True:
            texto=input(f"{Comentario}:\n")
            if cls.validar_palabra_alfabetico(texto):
                return texto
                break  
            else:
                print("Error-El texto ingresado contiene caracteres numericos")
           
    @staticmethod
    def validar_palabra_alfabetico(texto):
        valor_de_verdad=True
        lista_texto=texto.split(" ")
        for palabra in lista_texto:
            if palabra.isalpha():
                valor_de_verdad=True  
            else:
                valor_de_verdad=True
        return valor_de_verdad

    @classmethod
    def validar_dni(cls,Comentario):
        dni=""
        while True:
            dni=input(f"{Comentario}:\n")
            if len(dni)==8 and cls.validar_caracter_numero(dni):
                return dni
                break
            else:
                if not(len(dni)==8):
                    print('''Error: El DNI tiene ingresado no tiene 8 caracteres''')
                if not(cls.validar_caracter_numero(dni)):
                    print('''Error: El DNI ingresado tiene caracteres alfabeticos''')
              
    @staticmethod
    def validar_caracter_numero(texto):
        valor_de_Verdad=True
        for caracter in texto:
            try: 
                caracter_int=int(caracter)
            except ValueError:
                valor_de_Verdad=False
        return valor_de_Verdad

    @staticmethod
    def validar_edad(Comentario):
        edad=''
        while True:
            try:
                while True:
                    edad=int(input(f"{Comentario}:\n"))
                    if edad>=0 and edad<=100:
                        return edad
                    else:
                        print("Error-Ingrese una edad entre 0 a 100")
                break
            
            except ValueError:
                print(f'Error-Ingrese un numero valido')
    @classmethod
    def validar_codigo(cls,tipo):
        
        while True:
            codigo=input(f"ingrese codigo de {tipo}:\n")
            if(tipo =='curso'):
                cc=array_curso()
                if cls.validar_codigo_curso(codigo):
                    cc.eliminar(cc.buscar(codigo))
                    break
            elif(tipo =='alumno'):
                aa=array_alumno()  
                if cls.validar_codigo_alumno(codigo):
                    aa.eliminar(aa.buscar(codigo))
                    break
            elif(tipo =='docente'):
                dd=array_docente()  
                if cls.validar_codigo_docente(codigo):
                    dd.eliminar(dd.buscar(codigo))
                    break
            elif(tipo =='nota'):
                nn=array_nota()  
                if cls.validar_codigo_nota(codigo):
                    nn.eliminar(nn.buscar(codigo))
                    break  
            else:
                print(f"Erro codigo de {tipo} invalido\n")


    @staticmethod
    def validar_codigo_curso(codigo_ingresado):
        cc=array_curso()
        lista_de_cursos=cc.lista_curso
        valor_de_Verdad=False
        for curso in lista_de_cursos:
            diccionario_curso=curso.__dict__
            if(diccionario_curso.get('cod_curso')==codigo_ingresado):
                valor_de_Verdad=True
        return valor_de_Verdad

    @staticmethod
    def validar_codigo_alumno(codigo_ingresado):
        aa=array_alumno()
        lista_de_alumno=aa.lista_alumno
        valor_de_Verdad=False
        for alumno in lista_de_alumno:
            diccionario_alumno=alumno.__dict__
            if(diccionario_alumno.get('cod_alumno')==codigo_ingresado):
                valor_de_Verdad=True
        return valor_de_Verdad
    @staticmethod
    def validar_codigo_docente(codigo_ingresado):
        dd=array_docente()
        lista_de_docente=dd.lista_docente
        valor_de_Verdad=False
        for docente in lista_de_docente:
            diccionario_docente=docente.__dict__
            if(diccionario_docente.get('cod_docente')==codigo_ingresado):
                valor_de_Verdad=True
        return valor_de_Verdad
    @staticmethod
    def validar_codigo_nota(codigo_ingresado):
        nn=array_nota()
        lista_de_nota=nn.lista_nota
        valor_de_Verdad=False
        for nota in lista_de_nota:
            diccionario_nota=nota.__dict__
            if(diccionario_nota.get('cod_nota')==codigo_ingresado):
                valor_de_Verdad=True
        return valor_de_Verdad
