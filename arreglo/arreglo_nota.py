from clases.nota import Nota

class array_nota:
#CRUD: Create, Read, Update, Delete 
    # Create METODO CONSTRUCTOR
    def __init__(self):
        
        self.lista_nota = []
        self.leer_txt()
        
    
    def tamano(self):
        return len(self.lista_nota)
    
    # Update
    def agregar(self, Nota):
        self.lista_nota.append(Nota)
        self.grabar_txt()
    
    # Read
    def obtener(self,pos):
        return self.lista_nota[pos]
    
    # Read
    def buscar(self, codigo_nota):
        for nota in self.lista_nota:
            diccionario_nota=nota.__dict__
            if(diccionario_nota.get('cod_nota')==codigo_nota):
                return nota
    
    # Delete
    def eliminar(self, Nota):
        self.lista_nota.remove(Nota)
        self.grabar_txt()

############################################################################
# Leer el archivo de texto y crear los objetos e incluirlo dentro del Array
############################################################################
    def leer_txt(self):
        try:
            file = open('nota.txt', 'r', encoding='utf-8')
            for linea in file.readlines():
                if file.readlines()!='':
                    valor= linea.split(";")
                    self.lista_nota.append(Nota(valor[0],valor[1],valor[2],valor[3],valor[4],valor[5],valor[6]))
        
        except OSError as e:
            file = open('nota.txt', 'x', encoding='utf-8')
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

            file=open('nota.txt', 'w', encoding='utf-8')
            for nota in self.lista_nota:
                diccionario_nota=nota.__dict__
                texto=''
                total=len(diccionario_nota)
                i=1
                for key, value in diccionario_nota.items():
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
            return '7000'
        else:
            return int(self.obtener(self.tamano()-1).__dict__.get('cod_nota'))+1




