import numpy as np

class Bucket:
    __arreglo = None
    __contador = None

    def __init__(self, tamanio = 20):
        self.__arreglo = np.zeros(tamanio, dtype= int)
        self.__contador = 0
    
    def insertar(self, elemento):
        band = False
        if elemento in self.__arreglo:#Verifica si el elemento está en el arreglo
            band = True
            print('ERROR: Elemento ya existente!')

        elif self.__contador < len(self.__arreglo):
                band = True
                self.__arreglo[self.__contador] = elemento
                self.__contador+=1
    
        return band
    
    def buscar(self, elemento):
        band = False
        if elemento in self.__arreglo:
            band = True
        return band

    def getCantElementos(self):
        return self.__contador 
    
    
    def __str__(self):
        s = ''
        if self.__contador != 0:
            for i in range(self.__contador):
                s+= str(self.__arreglo[i])+'--'
        return '[' + s + ']'
        
    
