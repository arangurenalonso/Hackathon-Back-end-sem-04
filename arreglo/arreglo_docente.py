from clases.docente import Docente

class array_docente:
#CRUD: Create, Read, Update, Delete 
    # Create METODO CONSTRUCTOR
    def __init__(self):
        
        self.lista_docente = []
        self.leer_txt()
        
    
    def tamano(self):
        return len(self.lista_docente)
    
    # Update
    def agregar(self, Docente):
        self.lista_docente.append(Docente)
        self.grabar_txt()
    
    # Read
    def obtener(self,pos):
        return self.lista_docente[pos]
    
    # Read
    def buscar(self, codigo_docente):
        for docente in self.lista_docente:
            diccionario_docente=docente.__dict__
            if(diccionario_docente.get('cod_docente')==codigo_docente):
                return docente
    
    # Delete
    def eliminar(self, Docente):
        self.lista_docente.remove(Docente)
        self.grabar_txt()

############################################################################
# Leer el archivo de texto y crear los objetos e incluirlo dentro del Array
############################################################################
    def leer_txt(self):
        try:
            file = open('docente.txt', 'r', encoding='utf-8')
            for linea in file.readlines():
                if file.readlines()!='':
                    valor= linea.split(";")
                    self.lista_docente.append(Docente(valor[0],valor[1],valor[2],valor[3],valor[4],valor[5]))
        
        except OSError as e:
            file = open('docente.txt', 'x', encoding='utf-8')
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

            file=open('docente.txt', 'w', encoding='utf-8')
            for docente in self.lista_docente:
                diccionario_docente=docente.__dict__
                texto=''
                total=len(diccionario_docente)
                i=1
                for key, value in diccionario_docente.items():
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
            return '20000'
        else:
            return int(self.obtener(self.tamano()-1).__dict__.get('cod_docente'))+1

