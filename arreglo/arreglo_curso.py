from clases.curso import Curso

class array_curso:
#CRUD: Create, Read, Update, Delete 
    # Create METODO CONSTRUCTOR
    def __init__(self):
        
        self.lista_curso = []
        self.leer_txt()
        
    
    def tamano(self):
        return len(self.lista_curso)
    
    # Update
    def agregar(self, Curso):
        self.lista_curso.append(Curso)
        self.grabar_txt()
    
    # Read
    def obtener(self,pos):
        return self.lista_curso[pos]
    
    # Read
    def buscar(self, codigo_curso):
        for curso in self.lista_curso:
            diccionario_curso=curso.__dict__
            if(diccionario_curso.get('cod_curso')==codigo_curso):
                return curso
    
    # Delete
    def eliminar(self, Curso):
        self.lista_curso.remove(Curso)
        self.grabar_txt()

############################################################################
# Leer el archivo de texto y crear los objetos e incluirlo dentro del Array
############################################################################
    def leer_txt(self):
        try:
            file = open('curso.txt', 'r', encoding='utf-8')
            for linea in file.readlines():
                if file.readlines()!='':
                    valor= linea.split(";")
                    self.lista_curso.append(Curso(valor[0],valor[1]))
        
        except OSError as e:
            file = open('curso.txt', 'x', encoding='utf-8')
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

            file=open('curso.txt', 'w', encoding='utf-8')
            for curso in self.lista_curso:
                diccionario_curso=curso.__dict__
                texto=''
                total=len(diccionario_curso)
                i=1
                for key, value in diccionario_curso.items():
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
        if(self.tamano()==0):
            return '56000'
        else:
            return int(self.obtener(self.tamano()-1).__dict__.get('cod_curso'))+1




