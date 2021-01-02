from clases.alumno import Alumno

class array_alumno:
#CRUD: Create, Read, Update, Delete 
    # Create METODO CONSTRUCTOR
    def __init__(self):
        
        self.lista_alumno = []
        self.leer_txt()
        
    
    def tamano(self):
        return len(self.lista_alumno)
    
    # Update
    def agregar(self, Alumno):
        self.lista_alumno.append(Alumno)
        self.grabar_txt()
    
    # Read
    def obtener(self,pos):
        return self.lista_alumno[pos]
    
    # Read
    def buscar(self, codigo_alumno):
        for alumno in self.lista_alumno:
            diccionario_alumno=alumno.__dict__
            if(diccionario_alumno.get('cod_alumno')==codigo_alumno):
                return alumno
    
    # Delete
    def eliminar(self, alumno):
        self.lista_alumno.remove(alumno)
        self.grabar_txt()

############################################################################
# Leer el archivo de texto y crear los objetos e incluirlo dentro del Array
############################################################################
    def leer_txt(self):
        try:
            file = open('alumno.txt', 'r', encoding='utf-8')
            for linea in file.readlines():
                if file.readlines()!='':
                    valor= linea.split(";")
                    self.lista_alumno.append(Alumno(valor[0],valor[1],valor[2],valor[3],valor[4]))
        
        except OSError as e:
            file = open('alumno.txt', 'x', encoding='utf-8')
        except Exception as e:
            print('Hola')
            print(f'error: {str(e)}')
        finally:
            if file:
                file.close()
    
    
############################################################################
# Leer el archivo de texto y crear los objetos e incluirlo dentro del Array
############################################################################
    def grabar_txt(self):
        try:

            file=open('alumno.txt', 'w', encoding='utf-8')
            for alumno in self.lista_alumno:
                diccionario_alumno=alumno.__dict__
                texto=''
                total=len(diccionario_alumno)
                i=1
                for key, value in diccionario_alumno.items():
                    texto +=f'{value}'
                    i+=1
                    if i<=total:
                        texto += ';'
                    else:
                        texto += '; \n'
                file.write(texto)
        except Exception as e:
            print(f'error: {e}')
        finally:
            if file:
                file.close() 




############################################################################
#                       Otros Metodos
############################################################################
    def codigo_correlativo(self):
        if(len(self.lista_alumno)==0):
            return '202100001'
        else:
            return int(self.obtener(self.tamano()-1).__dict__.get('cod_alumno'))+1




