import math
import random
import numpy as np
from claseBucket import Bucket

class TablaHash:
    __arreglo = None
    __zonaPrimaria = None
    __zonaSecundaria = None
    __overflowActual = None
    __cantClaves = None
    __bucketsDesbordados = None
    __bucketsSubocupados = None

    def __init__(self, tamanio = 1000):
        self.__cantClaves = tamanio
        tamanio = math.floor(self.__cantClaves/20)
        while not self.es_primo(tamanio):
            tamanio+=1
        self.__zonaPrimaria = tamanio
        self.__zonaSecundaria = math.floor(tamanio*(0.30))
        self.__arreglo = np.empty(self.__zonaPrimaria+self.__zonaSecundaria,dtype = Bucket)
        self.__overflowActual = self.__zonaPrimaria+1
        self.__bucketsDesbordados = 0
        self.__bucketsSubocupados = 0
        for i in range(len(self.__arreglo)):
            self.__arreglo[i] = Bucket(20)
     

    def es_primo(self, numero):
        n = 2
        band = True
        while band and n < numero:
            if numero % n == 0:
                band = False

            else:
                n+=1
        return band
    
    def getDireccion(self, clave):
        indice = int(str(clave)[-2:])
        
        while indice >= self.__zonaPrimaria:
            indice = indice%self.__zonaPrimaria
        return indice

    def insertar(self, clave):
        direccion = self.getDireccion(clave)
        if not self.__arreglo[direccion].insertar(clave): #Verifica si el bucket  está lleno, Si está lleno, retornará False y no insertará el elemento
            self.__bucketsDesbordados +=1
            if not self.__arreglo[self.__overflowActual].insertar(clave):#Verifica si el bucket actual de la zona de overflow esta lleno
                if self.__overflowActual < len(self.__arreglo):#Verifica si llego al último bucket de la zona overflow
                    self.__overflowActual += 1
                    self.__arreglo[self.__overflowActual].insertar(clave)
                else:
                    print('ERROR: Arreglo lleno!')

    def getBucketsSubocupados(self):
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getCantElementos() < math.floor(20/3):#Verifica si los buckets tienen menos de su tercera parte ocupada
                self.__bucketsSubocupados+=1
        return self.__bucketsSubocupados

    def getBucketsDesbordados(self):
        return self.__bucketsDesbordados

    def recorrer(self):
        for i in range(self.__zonaPrimaria):
            if str(self.__arreglo[i]) != '[]':
                print(self.__arreglo[i])
        print('Zona secundaria (Overflow)')
        for j in range(self.__zonaPrimaria, len(self.__arreglo),+1):
            if str(self.__arreglo[j]) != '[]':
                print(self.__arreglo[j])
    
    def buscar(self, clave):
        direccion = self.getDireccion(clave)
        pos = None
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].buscar(clave):
                pos = i
        return pos


